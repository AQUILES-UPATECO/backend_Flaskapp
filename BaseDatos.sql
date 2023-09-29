CREATE DATABASE chatapp;
USE chatapp;
-- Crear la tabla Usuarios
CREATE TABLE Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL,  
    contrasena VARCHAR(60),  -- Tamaño adecuado para el hash bcrypt
    correo_electronico VARCHAR(100),
    imagen_perfil VARCHAR(255)
);
 

-- Crear la tabla Servidores
CREATE TABLE Servidores (
    id_servidor INT AUTO_INCREMENT PRIMARY KEY,
    nombre_servidor VARCHAR (255) NOT NULL,
    descripcion_servidor VARCHAR (255),
    id_usuario INT,
    id_usuario_creador INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);
-- Crear la tabla Usuario_Servidor para representar la relación entre Usuario y Servidor
CREATE TABLE Usuario_Servidor (
    Id_usuario INT,
    Id_servidor INT,
    PRIMARY KEY (id_usuario, id_servidor),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_servidor) REFERENCES Servidores(id_servidor)
);
-- Crear la tabla Canal
CREATE TABLE Canales (
    id_canal INT AUTO_INCREMENT PRIMARY KEY,
    nombre_canal VARCHAR(50) NOT NULL,
    descripcion_canal VARCHAR(255),
    imagen_canal VARCHAR (255),
    id_servidor INT,
    id_usuario INT,        
    FOREIGN KEY (id_servidor) REFERENCES Servidores(id_servidor),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)    
);
-- Crear la tabla Mensaje
CREATE TABLE Mensajes (
    id_mensaje INT AUTO_INCREMENT PRIMARY KEY,
    contenido_mensaje TEXT NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL,
    id_usuario INT,
    id_canal INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_canal) REFERENCES Canales(id_canal)
);

--PRIMERO DEBES REGISTRAR UN USUARIO Y CON EL ID DE ESE USUARIO SE CREARAN LOS SERVIDORES

--Servidores de Ejemplo


-- Servidor 1: Ciencia y Tecnología
INSERT INTO Servidores (nombre_servidor, descripción_servidor, id_usuario)
VALUES ('Ciencia y Tecnología', 'Discusión sobre los últimos avances en ciencia y tecnología.', 1);

-- Servidor 2: Viajes y Aventuras
INSERT INTO Servidores (nombre_servidor, descripción_servidor, id_usuario)
VALUES ('Viajes y Aventuras', 'Comparte tus experiencias de viajes y aventuras.', 1);

-- Servidor 3: Cine y Series
INSERT INTO Servidores (nombre_servidor, descripción_servidor, id_usuario)
VALUES ('Cine y Series', 'Debate sobre tus películas y series favoritas.', 1);

-- Servidor 4: Música en Español
INSERT INTO Servidores (nombre_servidor, descripción_servidor, id_usuario)
VALUES ('Música en Español', 'Comparte y descubre música en español de diferentes géneros.', 1);

-- Servidor 5: Deportes
INSERT INTO Servidores (nombre_servidor, descripción_servidor, id_usuario)
VALUES ('Deportes', 'Conversación sobre eventos deportivos y noticias deportivas.', 1);
