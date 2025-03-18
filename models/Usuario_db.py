import uuid
from flask_login import UserMixin
from config.db import db

class Usuario(db.Model, UserMixin):
    '''Modelo db de Usuario'''
    id = db.Column(db.Integer, primary_key = True, default = str(uuid.uuid4))
    username = db.Column(db.Text, unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    es_admin = db.Column(db.Boolean, nullable = True)
    es_empleado = db.Column(db.Boolean, nullable = True)
