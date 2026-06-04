fastapi mongodb
Revisando la estructura del proyecto y los archivos existentes.

# fast-api-crud-mongodb

Proyecto de ejemplo: CRUD de productos usando FastAPI, MongoDB y Prisma.

## Video
- [YouTube](https://youtu.be/OBUv7sjukqc?si=Sfp-3ec19Mv_7Gzk)
- [Documento](https://docs.google.com/document/d/144L7hnqZtcj_vs6ha6f4fB_QHJzgXdH2BbwSnNrFwrQ/edit?usp=sharing)

## Estructura del proyecto

- `main.py`: archivo principal para correr la API con Uvicorn.
- `config/prisma_config.py`: inicializa el cliente Prisma y carga variables de entorno.
- `prisma/schema.prisma`: esquema de Prisma para MongoDB.
- `rutas/rutas_producto.py`: rutas REST para productos (GET, POST, PUT, DELETE).
- `esquema/producto_esquema.py`: modelos Pydantic para validación.
- `servicios/producto_servicio.py`: lógica de negocio y acceso a datos.
- `templates/`: plantillas Jinja para la interfaz de CRUD.
- `static/style.css`: estilos para la página principal.
- `.env`: configuración de conexión a MongoDB.
- `.gitignore`: archivos y carpetas ignorados por Git.
- `requerimientos.txt`: dependencias del proyecto.

## Modelo de Producto

Campos:
- `id`: string
- `titulo`: string
- `categoria`: string
- `precio`: float
- `descripcion`: string

## Cómo ejecutar

1. Crear y activar el entorno virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requerimientos.txt
   ```

3. Configurar MongoDB en `.env`:
   ```env
   DATABASE_URL="mongodb://localhost:27017/fastapi_db?directConnection=true&replicaSet=rs0"
   ```

> Importante: Prisma con MongoDB requiere un servidor MongoDB corriendo como replica set para operaciones de escritura.

4. Iniciar MongoDB como replica set:

- Localmente:
  ```bash
  mongod --dbpath /var/lib/mongodb --replSet rs0 --bind_ip localhost
  ```

  Luego abrir `mongosh` y ejecutar:
  ```js
  rs.initiate()
  ```

- Con Docker:
  ```bash
  docker run -d --name mongodb -p 27017:27017 mongo:latest --replSet rs0
  docker exec -it mongodb mongosh --eval "rs.initiate()"
  ```

5. Generar el cliente Prisma:
   ```bash
   python -m prisma generate
   ```

6. Ejecutar la app con Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

7. Probar las rutas:
- `GET /productos`
- `GET /productos/{producto_id}`
- `POST /productos`
- `PUT /productos/{producto_id}`
- `DELETE /productos/{producto_id}`

## Ejemplo de payload para crear un producto

```json
{
  "titulo": "Camiseta",
  "categoria": "Ropa",
  "precio": 19.99,
  "descripcion": "Camiseta de algodón para uso diario"
}
```

## Notas

- Las rutas están en `rutas/rutas_producto.py`.
- La lógica de negocio está en `servicios/producto_servicio.py`.
- El archivo de Prisma usa MongoDB y debe generar el cliente antes de correr la API.
