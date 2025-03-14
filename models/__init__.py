from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar las clases de modelo y las listas de ejemplo
from .usuarios import Usuario, usuarios_ejemplo
from .drones import Dron, ejemplo_drones
