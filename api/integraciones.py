from flask import Blueprint, request, jsonify, send_file
from models import db, Consultante, Evaluacion
from utils.google_drive import GoogleDriveManager
from utils.pdf_generator import PDFGenerator
import os
import io
import tempfile

integraciones_bp = Blueprint('integraciones', __name__)


@integraciones_bp.route('/google-docs/<int:evaluacion_id>', methods=['POST'])
def crear_google_doc(evaluacion_id):
    """
    Crea un Google Doc automáticamente con la ficha del consultante

    Body (opcional):
    {
        "compartir_con": "email@example.com"  // Email para compartir (opcional)
    }
    """
    try:
        evaluacion = Evaluacion.query.get_or_404(evaluacion_id)
        consultante = Consultante.query.get(evaluacion.consultante_id)

        if not consultante:
            return jsonify({'error': 'Consultante no encontrado'}), 404

        # Obtener token de acceso (en producción, usar servicio de autenticación)
        google_token = os.getenv('GOOGLE_ACCESS_TOKEN')
        if not google_token:
            return jsonify({'error': 'Google Drive no está configurado. Solicita autorización al administrador.'}), 400

        # Crear cliente de Google Drive
        gd = GoogleDriveManager(access_token=google_token)

        # Crear ficha con datos de evaluación
        resultado_evaluacion = evaluacion.to_dict()

        doc_info = gd.crear_ficha_consultante(
            consultante.to_dict(),
            resultado_evaluacion
        )

        # Si se solicita, compartir con alguien
        data = request.get_json() or {}
        if data.get('compartir_con'):
            try:
                gd.compartir_documento(
                    doc_info['id'],
                    data['compartir_con'],
                    rol='reader'
                )
            except Exception as e:
                # Log pero no falla el request
                print(f"Advertencia: No se pudo compartir documento: {str(e)}")

        return jsonify({
            'success': True,
            'documento': doc_info,
            'mensaje': f'Ficha creada exitosamente en Google Drive'
        }), 201

    except Exception as error:
        return jsonify({'error': str(error)}), 500


@integraciones_bp.route('/pdf/<int:evaluacion_id>', methods=['GET'])
def descargar_pdf(evaluacion_id):
    """
    Descarga un PDF con los resultados de la evaluación
    """
    try:
        evaluacion = Evaluacion.query.get_or_404(evaluacion_id)
        consultante = Consultante.query.get(evaluacion.consultante_id)

        if not consultante:
            return jsonify({'error': 'Consultante no encontrado'}), 404

        # Generar PDF en memoria
        pdf_gen = PDFGenerator()
        pdf_bytes = pdf_gen.generar_ficha_evaluacion(
            consultante.to_dict(),
            evaluacion.to_dict()
        )

        # Nombre del archivo
        nombre_archivo = f"Ficha_{consultante.nombre}_{consultante.apellido}.pdf"

        # Enviar como descarga
        return send_file(
            io.BytesIO(pdf_bytes),
            mimetype='application/pdf',
            as_attachment=True,
            download_name=nombre_archivo
        )

    except Exception as error:
        return jsonify({'error': str(error)}), 500


@integraciones_bp.route('/drive/autorizar', methods=['POST'])
def autorizar_drive():
    """
    Endpoint para autorizar acceso a Google Drive (OAuth)

    Body:
    {
        "auth_code": "codigo_de_autorizacion"
    }
    """
    try:
        data = request.get_json()
        auth_code = data.get('auth_code')

        if not auth_code:
            return jsonify({'error': 'auth_code requerido'}), 400

        # Intercambiar código por token (implementación simplificada)
        # En producción, usar google-auth-oauthlib correctamente
        # Para ahora, retornar instrucción

        return jsonify({
            'status': 'pending',
            'message': 'Google Drive authorization flow iniciado',
            'instrucciones': [
                '1. Ve a: https://accounts.google.com/o/oauth2/v2/auth?...',
                '2. Autoriza el acceso a Drive',
                '3. Copia el código de autorización',
                '4. Envíalo en la próxima solicitud'
            ]
        }), 200

    except Exception as error:
        return jsonify({'error': str(error)}), 500


@integraciones_bp.route('/drive/config', methods=['GET'])
def obtener_config_drive():
    """
    Obtiene la configuración actual de Google Drive
    """
    folder_id = os.getenv('GOOGLE_DRIVE_FOLDER_ID')
    has_token = bool(os.getenv('GOOGLE_ACCESS_TOKEN'))

    return jsonify({
        'folder_id': folder_id,
        'carpeta_nombre': 'Consultantes IA' if folder_id else 'No configurada',
        'autorizado': has_token,
        'url_carpeta': f'https://drive.google.com/drive/folders/{folder_id}' if folder_id else None
    }), 200
