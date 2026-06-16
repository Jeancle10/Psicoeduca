from flask import Blueprint, jsonify
from models import Evaluacion, Consultante
from datetime import datetime, timedelta

resultados_bp = Blueprint('resultados', __name__)


@resultados_bp.route('/comparativa/<int:consultante_id>', methods=['GET'])
def comparativa_temporal(consultante_id):
    """
    Retorna comparativa temporal de evaluaciones de un consultante
    Útil para ver evolución
    """
    consultante = Consultante.query.get_or_404(consultante_id)
    evaluaciones = Evaluacion.query.filter_by(consultante_id=consultante_id).order_by(
        Evaluacion.fecha
    ).all()

    datos = {
        'consultante': consultante.to_dict(),
        'evaluaciones': [
            {
                'fecha': e.fecha.isoformat(),
                'stai_estado': e.stai_estado_puntuacion,
                'stai_rasgo': e.stai_rasgo_puntuacion,
                'bdi': e.bdi_puntuacion,
                'scl90': e.scl90_puntuacion
            }
            for e in evaluaciones
        ]
    }

    return jsonify(datos), 200


@resultados_bp.route('/estadisticas', methods=['GET'])
def estadisticas_generales():
    """
    Retorna estadísticas generales de todas las evaluaciones
    """
    todas_evaluaciones = Evaluacion.query.all()

    if not todas_evaluaciones:
        return jsonify({
            'total_evaluaciones': 0,
            'consultantes_evaluados': 0,
            'fecha_primer_registro': None,
            'fecha_ultimo_registro': None
        }), 200

    # Estadísticas STAI Estado
    stai_estado_scores = [e.stai_estado_puntuacion for e in todas_evaluaciones if e.stai_estado_puntuacion]
    stai_estado_promedio = sum(stai_estado_scores) / len(stai_estado_scores) if stai_estado_scores else 0

    # Estadísticas BDI
    bdi_scores = [e.bdi_puntuacion for e in todas_evaluaciones if e.bdi_puntuacion]
    bdi_promedio = sum(bdi_scores) / len(bdi_scores) if bdi_scores else 0

    # Estadísticas SCL-90
    scl90_scores = [e.scl90_puntuacion for e in todas_evaluaciones if e.scl90_puntuacion]
    scl90_promedio = sum(scl90_scores) / len(scl90_scores) if scl90_scores else 0

    # Distribución de categorías
    def contar_categorias(field):
        return {
            'SEVERO': len([e for e in todas_evaluaciones if getattr(e, field) == 'SEVERO']),
            'MODERADO': len([e for e in todas_evaluaciones if getattr(e, field) == 'MODERADO']),
            'LEVE': len([e for e in todas_evaluaciones if getattr(e, field) == 'LEVE']),
            'Ausente o Mínimo': len([e for e in todas_evaluaciones if getattr(e, field) == 'Ausente o Mínimo']),
            'Normal': len([e for e in todas_evaluaciones if getattr(e, field) == 'Normal'])
        }

    fechas = [e.fecha for e in todas_evaluaciones]

    return jsonify({
        'total_evaluaciones': len(todas_evaluaciones),
        'consultantes_evaluados': len(set(e.consultante_id for e in todas_evaluaciones)),
        'fecha_primer_registro': min(fechas).isoformat(),
        'fecha_ultimo_registro': max(fechas).isoformat(),
        'promedios': {
            'stai_estado': round(stai_estado_promedio, 2),
            'bdi': round(bdi_promedio, 2),
            'scl90': round(scl90_promedio, 2)
        },
        'distribucion_categorias': {
            'stai_estado': contar_categorias('stai_estado_categoria'),
            'bdi': contar_categorias('bdi_categoria'),
            'scl90': contar_categorias('scl90_categoria')
        }
    }), 200


@resultados_bp.route('/ultimas/<int:dias>', methods=['GET'])
def evaluaciones_ultimos_dias(dias):
    """
    Retorna evaluaciones de los últimos N días
    """
    fecha_desde = datetime.utcnow() - timedelta(days=dias)
    evaluaciones = Evaluacion.query.filter(Evaluacion.fecha >= fecha_desde).all()

    return jsonify([e.to_dict() for e in evaluaciones]), 200
