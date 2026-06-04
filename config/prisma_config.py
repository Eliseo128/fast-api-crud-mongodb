import os
from dotenv import load_dotenv
from prisma import Prisma

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("La variable de entorno DATABASE_URL no está definida en .env")

os.environ.setdefault("PRISMA_SCHEMA_PATH", "./prisma/schema.prisma")

db = Prisma()
