from app.models.usuarios import Usuario
import os
from flask import (    Blueprint,    request,    jsonify,)
from werkzeug.utils import secure_filename  # Para asegurarse de que el nombre de archivo sea seguro



usuarios_bp = Blueprint("usuarios", __name__)

# Directorio donde se guardarán las imágenes de perfil
UPLOAD_FOLDER = os.path.abspath('app/views/assets/profile_images')
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif"}  # Extensiones de archivo permitidas

# Función para verificar si la extensión del archivo es válida
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS



@usuarios_bp.route("/usuarios/registrar", methods=["POST"])
def registrar_usuario():

    # Obtener los datos del formulario JSON    
    nombre_usuario = request.form.get("nombre_usuario")
    contrasena = request.form.get("contrasena")
    correo_electronico = request.form.get("correo_electronico")
    imagen_perfil = request.files.get("imagen_perfil")

    # Manejar la carga de la imagen de perfil si se proporciona
    if imagen_perfil:
        if allowed_file(imagen_perfil.filename):
            filename = secure_filename(imagen_perfil.filename)
            imagen_perfil.save(os.path.join(UPLOAD_FOLDER, filename))
            print(filename)
        else:
            return jsonify({"message": "Formato de imagen no válido"}), 400

    # Llamar al método para registrar un nuevo usuario en el modelo
    Usuario.registrar_usuario(
        nombre_usuario, contrasena, correo_electronico, imagen_perfil.filename if imagen_perfil else None
    )

    return jsonify({"message": "Usuario registrado con éxito"}), 201


@usuarios_bp.route("/usuarios/iniciar_sesion", methods=["POST"])
def iniciar_sesion():
    data = request.json
    nombre_usuario = data.get("nombre_usuario")
    contrasena = data.get("contrasena")

    # Verificar el nombre de usuario y la contraseña
    usuario = Usuario.iniciar_sesion(nombre_usuario, contrasena)

    if usuario:
        # Usuario válido, ahora obtén los datos del usuario incluyendo el id_usuario
        datos_usuario = Usuario.obtener_datos_de_usuario(nombre_usuario)

        if datos_usuario:
            id_usuario, nombre_usuario, imagen_perfil = datos_usuario
            # Aquí puedes agregar la lógica para iniciar la sesión del usuario si es necesario
            # También puedes enviar el id_usuario como parte de la respuesta JSON
            return jsonify({"message": "Inicio de sesión exitoso", "nombre_usuario": nombre_usuario, "imagen_perfil": imagen_perfil, "id_usuario": id_usuario}), 200
        else:
            return jsonify({"message": "Error al obtener los datos del usuario"}), 500
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401
    


    

