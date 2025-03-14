from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from models.usuarios import Usuario
from models import db

login_bp = Blueprint('login', __name__, template_folder='templates')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Usuario.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_type'] = 'usuario'
            session['username'] = user.username
            flash(f'Bienvenido, {user.username}')
            return redirect(url_for('main.index'))
        flash('Credenciales incorrectas, por favor intente de nuevo.')
    return render_template('login.html')

@login_bp.route('/logout')
def logout():
    session.clear()
    flash('Has cerrado sesión.')
    return redirect(url_for('main.index'))

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if Usuario.query.filter((Usuario.username == username) | (Usuario.email == email)).first():
            flash('El nombre de usuario o correo ya existe.')
            return redirect(url_for('login.register'))
        new_user = Usuario(
            username=username,
            email=email,
            password=generate_password_hash(password),
            rol='usuario'
        )
        db.session.add(new_user)
        db.session.commit()
        flash('Usuario registrado exitosamente.')
        return redirect(url_for('login.login'))
    return render_template('register.html')
