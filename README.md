# fast-api-crud-mongodb
fastapi mongodb
Revisando la estructura del proyecto y los archivos existentes.



```
Verificando la sintaxis de los archivos Python recién creados.

Ran terminal command:  cd /workspaces/fast-api-crud-mongodb && python3 -m py_compile main.py config/prisma_config.py rutas/rutas_producto.py esquema/producto_esquema.py servicios/producto_servicio.py

## ✅ Proyecto creado

He creado una aplicación CRUD de FastAPI con Prisma y MongoDB usando la estructura solicitada:

- main.py
- prisma_config.py
- esquema_prisma.prisma
- rutas_producto.py
- producto_esquema.py
- producto_servicio.py
- .env
- .gitignore
- requerimientos.txt

También agregué los paquetes `__init__.py` necesarios en cada subcarpeta para que Python reconozca los paquetes.

---

## 🧠 Qué hace cada parte

- main.py: inicializa FastAPI, habilita CORS y arranca Uvicorn.
- prisma_config.py: carga .env, define la conexión Prisma y el cliente `db`.
- esquema_prisma.prisma: define el modelo `Producto` con `id`, `titulo`, `categoria`, `precio`, `descripcion`.
- producto_esquema.py: define los modelos Pydantic para validación y respuestas.
- producto_servicio.py: contiene la lógica de negocio y operaciones con la base de datos.
- rutas_producto.py: expone los endpoints REST:
  - `GET /productos`
  - `GET /productos/{producto_id}`
  - `POST /productos`
  - `PUT /productos/{producto_id}`
  - `DELETE /productos/{producto_id}`

---

## ▶️ Cómo ejecutar

1. Crear y activar el entorno virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requerimientos.txt
   ```

3. Asegurarse de tener MongoDB corriendo y actualizar .env si es necesario:
   ```env
   DATABASE_URL="mongodb://localhost:27017/fastapi_db"
   ```

4. Generar el cliente Prisma:
   ```bash
   python -m prisma generate
   ```

5. Ejecutar la API:
   ```bash
   uvicorn main:app --reload
   ```

---

## 💡 Nota para alumnos

Este proyecto separa claramente:
- rutas = endpoints
- servicios = lógica de negocio
- esquema = validación de datos
- config = configuración de la base de datos

Si quieres, puedo también agregar ejemplos de solicitudes `curl` para crear, listar, actualizar y borrar productos.

Se realizaron cambios.
