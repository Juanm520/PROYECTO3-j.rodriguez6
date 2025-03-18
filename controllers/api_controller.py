from flask import Blueprint, request
from models.Productos_db import Producto
from models.Ingredientes_db import Ingrediente

#API: ENDPOINTS
productos_blueprint = Blueprint('productos', __name__, url_prefix = '/productos')
producto_id_blueprint = Blueprint('producto_id', __name__, url_prefix = '/producto_id')
producto_nombre_blueprint = Blueprint('producto_nombre', __name__, url_prefix = '/producto_nombre')
producto_calorias_blueprint = Blueprint('producto_calorias', __name__, url_prefix = '/producto_calorias')
producto_rentabilidad_blueprint = Blueprint('producto_rentabilidad', __name__, url_prefix = '/producto_rentabilidad')
producto_costo_blueprint = Blueprint('producto_costo', __name__, url_prefix = '/producto_costo')
vender_producto_blueprint = Blueprint('vender_producto', __name__, url_prefix = '/vender_producto')
ingredientes_blueprint = Blueprint('ingredientes', __name__, url_prefix = 'ingredientes')
ingrediente_id_blueprint = Blueprint('ingrediente_id', __name__, url_prefix = 'ingrediente_id')
ingrediente_nombre_blueprint = Blueprint('ingrediente_nombre', __name__, url_prefix = 'ingrediente_nombre')
ingrediente_es_sano_blueprint = Blueprint('ingrediente_sano', __name__, url_prefix = 'ingrediente_sano')
ingrediente_reabastecer_blueprint = Blueprint('ingrediente_reabastecer', __name__, url_prefix = 'ingrediente_reabastecer')
ingrediente_renovar_blueprint = Blueprint('ingrediente_renovar', __name__, url_prefix = 'ingrediente_renovar')


#Deficiones de los EndPoints:
@productos_blueprint.route('/', method='GET')
def productos_controller():
    pass

@producto_id_blueprint.route('/', method='GET')
def producto_id_controller():
    producto_id = request.args.get('id')
    
@producto_nombre_blueprint.route('/', method='GET')
def producto_nombre_controller():
    producto_nombre = request.args.get('nombre')

@producto_calorias_blueprint.route('/', method='GET')
def producto_calorias_controller():
    producto_id = request.args.get('id')

@producto_rentabilidad_blueprint.route('/', method='GET')
def producto_rentabilidad_controller():
    producto_id = request.args.get('id')

@producto_costo_blueprint.route('/', method='GET')
def producto_costo_controller():
    producto_id = request.args.get('id')

@ingredientes_blueprint.route('/', method='GET')
def ingredientes_controller():
    pass

@ingrediente_id_blueprint.route('/', method='GET')
def ingrediente_id_controller():
    ingrediente_id = request.args.get('id')

@ingrediente_nombre_blueprint.route('/', method='GET')
def ingrediente_nombre_controller():
    ingrediente_nombre = request.args.get('id')

@ingrediente_es_sano_blueprint.route('/', method='GET')
def ingrediente_sano_controller():
    ingrediente_id = request.args.get('id')

@ingrediente_reabastecer_blueprint.route('/', method='GET')
def ingrediente_reabastecer_controller():
    ingrediente_id = request.args.get('id')

@ingrediente_renovar_blueprint.route('/', method='GET')
def ingrediente_renovar_controller():
    ingrediente_id = request.args.get('id')

