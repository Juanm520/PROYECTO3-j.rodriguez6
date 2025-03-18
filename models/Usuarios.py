import uuid
from flask_login import UserMixin
from config.db import db

class Usuario(db.model, UserMixin):
    '''Clase Usuario en Base de Datos'''
    id = db.Column(db.Integer, primary_key = True, default = str(uuid.uuid4))
    username = db.Column(db.Text, unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)
    
