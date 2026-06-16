from flask import Blueprint, request, jsonify
from datetime import datetime
from models import db, Consultante

consultantes_bp = Blueprint('consultantes', __name__)


@consultantes_bp.route('/', methods=['GET'])
def listar_consultantes():
    """Lista todos los consultantes con filtros opcionales"""
    nombre = request.args.get('nombre', '')
    edad_min = request.args.get('edad_min', type=int)
    edad_max = request.args.get('edad_max', type=int)

    query = Consultante.query

    if nombre:
        query = query.filter(
            (Consultante.nombre.ilike(f'%{nombre}%')) |
            (Consultante.apellido.ilike(f'%{nombre}%'))
        )

    consultantes = query.all()

    # Filtrar por edad si se especifica
    if edad_min or edad_max:
        consultantes = [
            c for c in consultantes
            if (edad_min is None or c.edad() >= edad_min) and
               (edad_max is None or c.edad() <= edad_max)
        ]

    return jsonify([c.to_dict() for c in consultantes]), 200


@consultantes_bp.route('/<int:id>', methods=['GET'])
def obtener_consultante(id):
    """Obtiene un consultante específico con su historial de evaluaciones"""
    consultante = Consultante.query.get_or_404(id)

    data = consultante.to_dict()
    data['evaluaciones'] = [e.to_dict() for e in consultante.evaluaciones]

    return jsonify(data), 200


@consultantes_bp.route('/', methods=['POST'])
def crear_consultante():
    """Crea un nuevo consultante"""
    data = request.get_json()

    try:
        fecha_nac = datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d').date()
    except (KeyError, ValueError):
        return jsonify({'error': 'fecha_nacimiento inválida (formato: YYYY-MM-DD)'}), 400

    consultante = Consultante(
        nombre=data.get('nombre', '').strip(),
        apellido=data.get('apellido', '').strip(),
        fecha_nacimiento=fecha_nac,
        celular=data.get('celular', '').strip(),
        email=data.get('email', '').strip() or None
    )

    try:
        db.session.add(consultante)
        db.session.commit()
        return jsonify(consultante.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@consultantes_bp.route('/<int:id>', methods=['PUT'])
def actualizar_consultante(id):
    """Actualiza datos de un consultante"""
    consultante = Consultante.query.get_or_404(id)
    data = request.get_json()

    if 'nombre' in data:
        consultante.nombre = data['nombre'].strip()
    if 'apellido' in data:
        consultante.apellido = data['apellido'].strip()
    if 'celular' in data:
        consultante.celular = data['celular'].strip()
    if 'email' in data:
        consultante.email = data['email'].strip() or None
    if 'fecha_nacimiento' in data:
        try:
            consultante.fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'error': 'fecha_nacimiento inválida'}), 400

    try:
        db.session.commit()
        return jsonify(consultante.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@consultantes_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_consultante(id):
    """Elimina un consultante y todas sus evaluaciones"""
    consultante = Consultante.query.get_or_404(id)

    try:
        db.session.delete(consultante)
        db.session.commit()
        return jsonify({'message': 'Consultante eliminado'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
