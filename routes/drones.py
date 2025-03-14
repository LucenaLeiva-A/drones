from flask import Blueprint, render_template, request, redirect, url_for
from config import db
from models.drones import Dron

main_bp = Blueprint('main', __name__)

# Ejemplo de endpoint para reservar
main_bp.route('/reservar/<int:dron_id>', methods=['POST'])
def reservar(dron_id):
    dron = Dron.query.get_or_404(dron_id)
    if dron.disponible:
        dron.disponible = False
        db.session.commit()
        return "Reserva exitosa"
    else:
        return "El dron no está disponible"