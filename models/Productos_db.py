from config.db import db
from config.marshmallow import ma

class Producto(db.Model):
    '''Modelo de Producto en la base de datos.'''
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.Text, nullable=False)
    precio_publico = db.Column(db.Float, nullable=False)
    ingrediente1 = db.Column(db.Text, db.ForeignKey('ingrediente.nombre'), nullable=False)
    ingrediente2 = db.Column(db.Text, db.ForeignKey('ingrediente.nombre'), nullable=False)
    ingrediente3 = db.Column(db.Text, db.ForeignKey('ingrediente.nombre'), nullable=False)
    tipo_de_producto = db.Column(db.Text, nullable=False)
    tipo_vaso = db.Column(db.Text, nullable=True)
    volumen = db.Column(db.Integer, nullable=True)

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        include_fk = True