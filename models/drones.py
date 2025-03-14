from . import db
from sqlalchemy import Column, Integer, String, Boolean

class Dron(db.Model):
    __tablename__ = 'drones'
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    imagen_url = db.Column(db.String(255))
    disponible = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f"<Dron {self.modelo}>"

ejemplo_drones = [
    Dron(modelo="DJI Mavic 3", descripcion="Descripción breve del dron.", imagen_url="/static/multimedia/imagenes drones/DJI-Mavic-3-featured4.jpg"),
    Dron(modelo="DJI AIR 2", descripcion="Descripción breve del dron.", imagen_url="/static/multimedia/imagenes drones/air 2.jpg"),
    Dron(modelo="DJI Avatar 2", descripcion="Descripción breve del dron.", imagen_url="/static/multimedia/imagenes drones/DJI-Avata-FPV-Drone-2.jpg"),
    Dron(modelo="DJI Mini 2", descripcion="Descripción breve del dron.", imagen_url="/static/multimedia/imagenes drones/mini 2.jpg"),
    Dron(modelo="DJI Inspire 2", descripcion="Descripción breve del dron.", imagen_url="/static/multimedia/imagenes drones/DJI-inspire-3-landscape1.jpg"),
]
