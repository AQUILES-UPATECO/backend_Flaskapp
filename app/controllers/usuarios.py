from app.models.usuarios import Usuario  

def obtener_perfil_usuario(usuario_id):
    # Lógica para obtener el perfil de usuario
    usuario = Usuario.obtener_usuario_por_id(usuario_id)
    if usuario:
        return {
            'id_usuario': usuario.id_usuario,
            'nombre_usuario': usuario.nombre_usuario,
            'correo_electronico': usuario.correo_electronico,
            'imagen_perfil': usuario.imagen_perfil
        }
    else:
        return None

def editar_perfil_usuario(usuario_id, datos_nuevos):
    # Lógica para editar el perfil de usuario
    exito = Usuario.editar_usuario(usuario_id, datos_nuevos)
    return {'exito': exito}

def buscar_usuarios(termino_busqueda):
    # Lógica para buscar usuarios
    usuarios = Usuario.buscar_usuarios(termino_busqueda)
    resultados = []
    for usuario in usuarios:
        resultados.append({
            'id_usuario': usuario.id_usuario,
            'nombre_usuario': usuario.nombre_usuario,
            'correo_electronico': usuario.correo_electronico,
            'imagen_perfil': usuario.imagen_perfil
        })
    return resultados