
# API de Gestión de Datos con Flask

Esta es una API sencilla desarrollada en Flask que permite gestionar datos almacenados en un archivo `data.csv`. Proporciona endpoints para consultar, agregar, actualizar y eliminar datos.

## Requisitos previos

- Python 3.9 o superior
- Docker y Docker Compose (opcional, para ejecución en contenedores)

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```

## Uso de la aplicación

### Ejecución local

1. Ejecuta el servidor Flask:
   ```bash
   python app.py
   ```
2. La API estará disponible en `http://localhost:8080`.

### Ejecución con Docker

1. Construye y ejecuta los contenedores con Docker Compose:
   ```bash
   docker-compose up --build
   ```
2. La API estará disponible en `http://localhost:8080`.

## Endpoints

### 1. Obtener datos

**GET** `/data`  
Devuelve todos los datos almacenados en el archivo `data.csv`.

- **Curl**:
  ```bash
  curl -X GET http://localhost:8080/data
  ```
- **Postman**: Haz una solicitud `GET` a `http://localhost:8080/data`.

### 2. Subir datos

**POST** `/upload`  
Agrega un nuevo dato al archivo.

- **Body (JSON)**:
  ```json
  {
    "new_data": "nuevo_dato"
  }
  ```
- **Curl**:
  ```bash
  curl -X POST http://localhost:8080/upload -H "Content-Type: application/json" -d '{"new_data": "nuevo_dato"}'
  ```
- **Postman**: Haz una solicitud `POST` a `http://localhost:8080/upload` con el cuerpo en formato JSON.

### 3. Actualizar datos

**PATCH** `/update`  
Actualiza un dato existente en el archivo.

- **Body (JSON)**:
  ```json
  {
    "old_data": "dato_existente",
    "new_data": "dato_nuevo"
  }
  ```
- **Curl**:
  ```bash
  curl -X PATCH http://localhost:8080/update -H "Content-Type: application/json" -d '{"old_data": "dato_existente", "new_data": "dato_nuevo"}'
  ```
- **Postman**: Haz una solicitud `PATCH` a `http://localhost:8080/update` con el cuerpo en formato JSON.

### 4. Eliminar datos

**DELETE** `/erase`  
Elimina un dato del archivo.

- **Query Parameter**: `data` (el dato a eliminar)
- **Curl**:
  ```bash
  curl -X DELETE "http://localhost:8080/erase?data=dato_a_eliminar"
  ```
- **Postman**: Haz una solicitud `DELETE` a `http://localhost:8080/erase` agregando `?data=dato_a_eliminar` en la URL.

## Errores comunes

- **404 Not Found**: El dato no existe en la base de datos.
- **400 Bad Request**: Falta información requerida en la solicitud.
- **500 Internal Server Error**: Error inesperado al leer o escribir en el archivo.

## Notas

- El archivo `data.csv` se crea automáticamente si no existe.
- Asegúrate de que el archivo sea escribible para evitar errores de permisos.

¡Listo! Ahora puedes usar la API para gestionar tus datos.