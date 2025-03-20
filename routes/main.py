from flask import Blueprint, render_template
from models.drones import Dron
from flask import render_template, Blueprint
from models import Dron, Comentario

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def index():
    drones = Dron.query.all()
    comentarios = Comentario.query.all()  # obtén todos los comentarios
    return render_template('index.html', drones=drones, comentarios=comentarios)
