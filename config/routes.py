from controllers.inicio_controller import inicio_blueprint
import controllers.api_controller as api

def register_routes(app):
    app.register_blueprint(inicio_blueprint)
    app.register_blueprint(api.productos_blueprint)
    app.register_blueprint(api.producto_id_blueprint)
    app.register_blueprint(api.producto_nombre_blueprint)
    app.register_blueprint(api.producto_calorias_blueprint)
    app.register_blueprint(api.producto_rentabilidad_blueprint)
    app.register_blueprint(api.producto_costo_blueprint)
    app.register_blueprint(api.vender_producto_blueprint)
    app.register_blueprint(api.ingredientes_blueprint)
    app.register_blueprint(api.ingrediente_id_blueprint)
    app.register_blueprint(api.ingrediente_nombre_blueprint)
    app.register_blueprint(api.ingrediente_es_sano_blueprint)
    app.register_blueprint(api.ingrediente_reabastecer_blueprint)
    app.register_blueprint(api.ingrediente_renovar_blueprint)
    
    