from flask import Blueprint, request, jsonify
from models import db, Consultante, Evaluacion
from tests_logic import procesar_todas_evaluaciones

evaluaciones_bp = Blueprint('evaluaciones', __name__)


@evaluaciones_bp.route('/<int:consultante_id>', methods=['GET'])
def obtener_evaluaciones_consultante(consultante_id):
    """Obtiene todas las evaluaciones de un consultante"""
    consultante = Consultante.query.get_or_404(consultante_id)
    evaluaciones = Evaluacion.query.filter_by(consultante_id=consultante_id).order_by(
        Evaluacion.fecha.desc()
    ).all()

    return jsonify([e.to_dict() for e in evaluaciones]), 200


@evaluaciones_bp.route('/<int:id>', methods=['GET'])
def obtener_evaluacion(id):
    """Obtiene una evaluación específica"""
    evaluacion = Evaluacion.query.get_or_404(id)
    return jsonify(evaluacion.to_dict()), 200


@evaluaciones_bp.route('/', methods=['POST'])
def crear_evaluacion():
    """
    Crea una nueva evaluación y procesa automáticamente los tests

    Formato esperado:
    {
        "consultante_id": 1,
        "respuestas": {
            "p1": "Juan García",
            "p2": "1990-05-15",
            "p3": "595999999",
            "p4": 2,
            "p5": 1,
            ... (hasta p135)
        }
    }
    """
    data = request.get_json()

    # Validar consultante existe
    consultante_id = data.get('consultante_id')
    if not consultante_id:
        return jsonify({'error': 'consultante_id requerido'}), 400

    consultante = Consultante.query.get_or_404(consultante_id)

    # Obtener respuestas
    respuestas = data.get('respuestas', {})
    if not respuestas:
        return jsonify({'error': 'respuestas requeridas'}), 400

    # Procesar todos los tests
    try:
        resultados = procesar_todas_evaluaciones(respuestas)
    except Exception as e:
        return jsonify({'error': f'Error procesando evaluación: {str(e)}'}), 400

    # Crear objeto Evaluacion
    evaluacion = Evaluacion(
        consultante_id=consultante_id,
    )
    evaluacion.set_respuestas(respuestas)

    # STAI Estado
    evaluacion.stai_estado_puntuacion = resultados['stai']['estado']['puntuacion']
    evaluacion.stai_estado_percentil = resultados['stai']['estado']['percentil']
    evaluacion.stai_estado_categoria = resultados['stai']['estado']['categoria']

    # STAI Rasgo
    evaluacion.stai_rasgo_puntuacion = resultados['stai']['rasgo']['puntuacion']
    evaluacion.stai_rasgo_percentil = resultados['stai']['rasgo']['percentil']
    evaluacion.stai_rasgo_categoria = resultados['stai']['rasgo']['categoria']

    # BDI
    evaluacion.bdi_puntuacion = resultados['bdi']['puntuacion']
    evaluacion.bdi_categoria = resultados['bdi']['categoria']

    # BFI-5
    evaluacion.bfi_neuroticismo = resultados['bfi']['neuroticismo']
    evaluacion.bfi_extraversion = resultados['bfi']['extraversion']
    evaluacion.bfi_apertura = resultados['bfi']['apertura']
    evaluacion.bfi_amabilidad = resultados['bfi']['amabilidad']
    evaluacion.bfi_responsabilidad = resultados['bfi']['responsabilidad']

    # SCL-90-R
    evaluacion.scl90_puntuacion = resultados['scl90']['puntuacion']
    evaluacion.scl90_categoria = resultados['scl90']['categoria']

    try:
        db.session.add(evaluacion)
        db.session.commit()
        return jsonify(evaluacion.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@evaluaciones_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_evaluacion(id):
    """Elimina una evaluación"""
    evaluacion = Evaluacion.query.get_or_404(id)

    try:
        db.session.delete(evaluacion)
        db.session.commit()
        return jsonify({'message': 'Evaluación eliminada'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
