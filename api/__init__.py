from flask import Blueprint

from .consultantes import consultantes_bp
from .evaluaciones import evaluaciones_bp
from .resultados import resultados_bp


def init_api(app):
    """Registra todos los blueprints de API"""
    app.register_blueprint(consultantes_bp, url_prefix='/api/consultantes')
    app.register_blueprint(evaluaciones_bp, url_prefix='/api/evaluaciones')
    app.register_blueprint(resultados_bp, url_prefix='/api/resultados')
