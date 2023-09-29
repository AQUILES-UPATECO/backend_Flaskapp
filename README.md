# backend_Flaskapp
BACKEND PARA TRABAJO FINAL DE LA CATEDRA DE PROGRAMACION 2, UPATECO-CIMNE-IBER -GRUPO 12-COMISION CN 

Este es el backend de mi proyecto, que sigue el patrón de arquitectura Modelo-Vista-Controlador (MVC). El backend se encarga de la lógica de negocio y la interacción con la base de datos.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **controllers:** En esta carpeta encontrarás controladores que manejan las solicitudes HTTP, procesan la lógica de negocio y gestionan las respuestas.

- **models:** Aquí se definen los modelos de datos que representan las tablas de la base de datos. Cada modelo tiene atributos y métodos para interactuar con la base de datos.

- **routes:** Las rutas o endpoints de la API se definen en esta carpeta. Aquí se especifica cómo se manejan las solicitudes HTTP, qué controladores se utilizan y qué datos se devuelven.

- **config:** En esta carpeta se encuentran datos de configuración que pueden contener información sensible como claves secretas, configuraciones de base de datos, etc.

- **init:** Código de inicialización que configuran y ejecutan la aplicación.

- **run.py:** Punto de entrada de la aplicación que inicia el servidor web.

## Requisitos y Dependencias

Para ejecutar el backend, asegúrate de tener instalado Python y las dependencias necesarias. Puedes encontrar una lista de dependencias en el archivo `requirements.txt`. Para instalarlas, usa:

## Configuración

Antes de ejecutar la aplicación, configura los parámetros necesarios en la carpeta `config`. Esto podría incluir configuraciones de base de datos, variables de entorno u otras configuraciones específicas.

## Ejecución
 
La aplicación estará disponible en [http://localhost:5000](http://localhost:5000) de manera predeterminada


¡Gracias porser parte de nuestro trayecto y proyecto Saludos!!