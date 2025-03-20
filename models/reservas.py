from . import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    drone_id = db.Column(db.Integer, db.ForeignKey('drones.id'), nullable=False, unique=True)  # cada dron solo se reserva una vez

    usuario = relationship("Usuario", backref="reservas")
    dron = relationship("Dron", backref="reserva")

    def __repr__(self):
        return f"<Reserva Usuario: {self.user_id} Dron: {self.drone_id}>"
