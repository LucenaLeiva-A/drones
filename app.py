from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Usuario, Dron, usuarios_ejemplo, ejemplo_drones
from routes.comentarios import comentarios_bp

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = '1234'  # Necesaria para sesiones y flash

# Inicializar la base de datos
db.init_app(app)

# Registrar Blueprints
from routes.main import main_bp
from routes.login import login_bp
from routes.reservas import reservas_bp
app.register_blueprint(reservas_bp)
app.register_blueprint(main_bp)
app.register_blueprint(login_bp)
app.register_blueprint(comentarios_bp)

def create_tables():
    with app.app_context():  # Asegúrate de que el contexto de la aplicación esté activo
        db.create_all()
        if not Dron.query.first():
            db.session.add_all(ejemplo_drones)
            db.session.commit()
        if not Usuario.query.first():
            db.session.add_all(usuarios_ejemplo)
            db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        create_tables()
    app.run(debug=True)