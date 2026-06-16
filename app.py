from flask import Flask, jsonify
import os
from models import db
from api import init_api

app = Flask(__name__)

# Configuración de BD
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://localhost/psicoeduca')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar BD
db.init_app(app)

# Registrar APIs
init_api(app)

# Health check
@app.route('/')
def health():
    return jsonify({
        "status": "ok",
        "app": "PsicoEduca API",
        "message": "Flask + PostgreSQL initialized",
        "version": "1.0"
    })

@app.route('/api/status')
def status():
    return jsonify({
        "status": "ready",
        "database": "connected" if test_db_connection() else "disconnected"
    })

def test_db_connection():
    try:
        db.session.execute('SELECT 1')
        return True
    except Exception:
        return False

# Crear tablas al iniciar
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
