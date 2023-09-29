from flask import Flask
from config import Config
from flask_cors import CORS
from app.routes.usuarios_routes import usuarios_bp
from app.routes.servidores_rutas import servidores_bp
from app.routes.canales_rutas import canales_bp
from app.routes.mensajes_rutas import mensajes_bp
from app.database import DatabaseConnection
from flask_login import LoginManager


def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(
        __name__,
        static_folder=Config.STATIC_FOLDER,
        template_folder=Config.TEMPLATE_FOLDER,
    )
    app.config.from_object(Config)
    DatabaseConnection.set_config(app.config)

    # Asignar la clave secreta directamente
    app.config["SECRET_KEY"] = Config.SECRET_KEY

    # Inicializar Flask-Login
    login_manager = LoginManager(app)

    # Configurar CORS con las opciones necesarias    
    cors = CORS(app, supports_credentials=True, origins='*')   # Habilitar el uso de credenciales (cookies, autenticación)

    # Registrar el Blueprint de usuarios
    app.register_blueprint(usuarios_bp)

    # Registrar el Blueprint de servidores
    app.register_blueprint(servidores_bp)

    # Registrar el Blueprint de canales
    app.register_blueprint(canales_bp)

    # Registrar el Blueprint de canales
    app.register_blueprint(mensajes_bp)

    return app
