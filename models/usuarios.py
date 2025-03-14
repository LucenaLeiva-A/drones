from . import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    rol = db.Column(db.String(50), nullable=False, default='usuario')
    
    def __repr__(self):
        return f"<Usuario {self.username}>"

usuarios_ejemplo = [
    Usuario(
        username="admin",
        password=generate_password_hash("1234"),
        email="admin@example.com",
        rol='admin'
    ),
    Usuario(
        username="usuario1",
        password=generate_password_hash("pass1"),
        email="usuario1@example.com",
        rol='usuario'
    ),
    Usuario(
        username="usuario2",
        password=generate_password_hash("pass2"),
        email="usuario2@example.com",
        rol='usuario'
    )
]
