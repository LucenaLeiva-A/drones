from flask import Blueprint, render_template
from models.drones import Dron

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def index():
    drones = Dron.query.all()
    return render_template('index.html', drones=drones)
