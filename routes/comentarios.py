from flask import Blueprint, request, jsonify, session, redirect, url_for, flash
from models import db
from models.comentarios import Comentario
from models.usuarios import Usuario

comentarios_bp = Blueprint('comentarios', __name__, url_prefix='/comentarios')

@comentarios_bp.route('/agregar', methods=['POST'])
def agregar_comentario():
    # Verificar si hay un usuario en sesión
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'Debes iniciar sesión para comentar.'})

    data = request.get_json()
    texto = data.get('comentario')
    if not texto:
        return jsonify({'success': False, 'error': 'El comentario no puede estar vacío.'})

    # Crear y guardar el comentario
    user = Usuario.query.get(session['user_id'])
    nuevo_comentario = Comentario(usuario_id=user.id, texto=texto)
    db.session.add(nuevo_comentario)
    db.session.commit()
    
    return jsonify({'success': True})

@comentarios_bp.route('/eliminar_comentario/<int:comentario_id>', methods=['POST'])
def eliminar_comentario(comentario_id):
    try:
        # Tu lógica para eliminar el comentario de la base de datos
        comentario = Comentario.query.get_or_404(comentario_id)
        db.session.delete(comentario)
        db.session.commit()
        
        flash('Comentario eliminado exitosamente', 'success')
        return redirect(url_for('main.index'))  # O la ruta donde quieras redirigir
    except Exception as e:
        flash('Error al eliminar el comentario', 'error')
        return redirect(url_for('main.index'))
