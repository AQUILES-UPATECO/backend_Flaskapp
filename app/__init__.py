from flask import Flask
from config import Config

from .routes.autenticacion_routes import autenticacion_routes
from .routes.servidores_routes import servidores_routes
from .routes.mensajes_routes import mensajes_routes
from .routes.canales_routes import canales_routes
from .routes.usuarios_routes import usuarios_routes


from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    
    app.config.from_object(Config)

    DatabaseConnection.set_config(app.config)

    # Registrar las rutas de autenticación
    app.register_blueprint(autenticacion_routes, url_prefix='/auth')

    # Registrar las rutas de gestión de servidores
    app.register_blueprint(servidores_routes, url_prefix='/servidores')

    # Registrar las rutas de gestión de servidores
    app.register_blueprint(canales_routes, url_prefix='/canales')

    # Registrar las rutas de gestión de mensajes
    app.register_blueprint(mensajes_routes, url_prefix='/mensajes')

    # Registrar las rutas de gestión de usuarios, esto podriamos revisarlo si es posible
    app.register_blueprint(usuarios_routes, url_prefix='/usuarios')
    

    return app