from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .usuarios import Usuario
from . import db  # Importa db desde el mismo directorio

class Comentario(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(Integer, primary_key=True)
    usuario_id = db.Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    texto = db.Column(Text, nullable=False)

    usuario = relationship("Usuario", backref="comentarios")

    def __repr__(self):
        return f"<Comentario {self.id}>"