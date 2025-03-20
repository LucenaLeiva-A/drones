from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for, flash
from models import db, Dron, Usuario, Reserva

reservas_bp = Blueprint('reservas', __name__, url_prefix='/reservas')

@reservas_bp.route('/')
def reservas():
    if 'user_id' not in session:
        flash("Debes iniciar sesión para ver tus reservas.")
        return redirect(url_for('login.login'))
    user_id = session['user_id']
    # Si el usuario es admin, se muestran todas las reservas; de lo contrario, solo las propias.
    if session.get('rol') == 'admin':
        reservas_list = Reserva.query.all()
    else:
        reservas_list = Reserva.query.filter_by(user_id=user_id).all()
    # Se obtiene el dron asociado a cada reserva
    drones_reservados = [reserva.dron for reserva in reservas_list]
    return render_template('reservas.html', drones=drones_reservados)

@reservas_bp.route('/reservar', methods=['POST'])
def reservar():
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'Debes iniciar sesión para reservar.'})
    user_id = session['user_id']
    data = request.get_json()
    drone_id = data.get('drone_id')
    if not drone_id:
        return jsonify({'success': False, 'error': 'No se proporcionó el ID del dron.'})
    drone = Dron.query.get(drone_id)
    if not drone:
        return jsonify({'success': False, 'error': 'Dron no encontrado.'})
    # Verificar si el dron ya tiene una reserva
    existing_reserva = Reserva.query.filter_by(drone_id=drone_id).first()
    if existing_reserva:
        return jsonify({'success': False, 'error': 'El dron ya ha sido reservado.'})
    # Crear la nueva reserva
    nueva_reserva = Reserva(user_id=user_id, drone_id=drone_id)
    db.session.add(nueva_reserva)
    # Marcar el dron como no disponible
    drone.disponible = False
    db.session.commit()
    return jsonify({'success': True})

@reservas_bp.route('/eliminar_reserva', methods=['POST'])
def eliminar_reserva():
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'Debes iniciar sesión.'})
    user_id = session['user_id']
    data = request.get_json()
    drone_id = data.get('drone_id')
    if not drone_id:
        return jsonify({'success': False, 'error': 'No se proporcionó el ID del dron.'})
    reserva = Reserva.query.filter_by(drone_id=drone_id).first()
    if not reserva:
        return jsonify({'success': False, 'error': 'Reserva no encontrada.'})
    # Solo el propietario de la reserva o el administrador pueden eliminarla
    if reserva.user_id != user_id and session.get('rol') != 'admin':
        return jsonify({'success': False, 'error': 'No tienes permiso para eliminar esta reserva.'})
    # Eliminar la reserva y liberar el dron
    db.session.delete(reserva)
    drone = Dron.query.get(drone_id)
    if drone:
        drone.disponible = True
    db.session.commit()
    return jsonify({'success': True})
