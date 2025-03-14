import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Base de datos SQLite en el archivo "cielo_digital.db"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'cielo_digital.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'clave_secreta_para_flask'
