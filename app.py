from flask import Flask, jsonify, render_template
import os
from models import db
from api import init_api

app = Flask(__name__, template_folder='templates', static_folder='static')

# Configuración de BD
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://localhost/psicoeduca')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar BD
db.init_app(app)

# Registrar APIs
init_api(app)

# Frontend
@app.route('/')
def index():
    return render_template('index.html')

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

# CORS (permitir requests desde el frontend)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# Crear tablas al iniciar
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
