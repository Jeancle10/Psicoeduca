from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Consultante(db.Model):
    __tablename__ = 'consultantes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    evaluaciones = db.relationship('Evaluacion', backref='consultante', lazy=True, cascade='all, delete-orphan')

    def edad(self):
        from datetime import date
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'fecha_nacimiento': self.fecha_nacimiento.isoformat(),
            'edad': self.edad(),
            'celular': self.celular,
            'email': self.email,
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'total_evaluaciones': len(self.evaluaciones)
        }


class Evaluacion(db.Model):
    __tablename__ = 'evaluaciones'

    id = db.Column(db.Integer, primary_key=True)
    consultante_id = db.Column(db.Integer, db.ForeignKey('consultantes.id'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    # Respuestas crudas (almacenadas como JSON)
    respuestas_json = db.Column(db.Text, nullable=False)

    # STAI - Estado (P4-P23)
    stai_estado_puntuacion = db.Column(db.Integer)
    stai_estado_percentil = db.Column(db.Integer)
    stai_estado_categoria = db.Column(db.String(50))

    # STAI - Rasgo (P24-P43)
    stai_rasgo_puntuacion = db.Column(db.Integer)
    stai_rasgo_percentil = db.Column(db.Integer)
    stai_rasgo_categoria = db.Column(db.String(50))

    # BDI (P44-P66)
    bdi_puntuacion = db.Column(db.Integer)
    bdi_categoria = db.Column(db.String(50))

    # BFI-5 (P67-P71)
    bfi_neuroticismo = db.Column(db.Float)
    bfi_extraversion = db.Column(db.Float)
    bfi_apertura = db.Column(db.Float)
    bfi_amabilidad = db.Column(db.Float)
    bfi_responsabilidad = db.Column(db.Float)

    # SCL-90-R (P72-P135)
    scl90_puntuacion = db.Column(db.Integer)
    scl90_categoria = db.Column(db.String(50))

    def respuestas_dict(self):
        return json.loads(self.respuestas_json)

    def set_respuestas(self, respuestas):
        self.respuestas_json = json.dumps(respuestas)

    def to_dict(self):
        return {
            'id': self.id,
            'consultante_id': self.consultante_id,
            'fecha': self.fecha.isoformat(),
            'stai_estado': {
                'puntuacion': self.stai_estado_puntuacion,
                'percentil': self.stai_estado_percentil,
                'categoria': self.stai_estado_categoria
            },
            'stai_rasgo': {
                'puntuacion': self.stai_rasgo_puntuacion,
                'percentil': self.stai_rasgo_percentil,
                'categoria': self.stai_rasgo_categoria
            },
            'bdi': {
                'puntuacion': self.bdi_puntuacion,
                'categoria': self.bdi_categoria
            },
            'bfi': {
                'neuroticismo': self.bfi_neuroticismo,
                'extraversion': self.bfi_extraversion,
                'apertura': self.bfi_apertura,
                'amabilidad': self.bfi_amabilidad,
                'responsabilidad': self.bfi_responsabilidad
            },
            'scl90': {
                'puntuacion': self.scl90_puntuacion,
                'categoria': self.scl90_categoria
            }
        }
