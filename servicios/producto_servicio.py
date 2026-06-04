from typing import List, Optional

from config.prisma_config import db
from esquema.producto_esquema import ProductoCreate, ProductoResponse, ProductoUpdate

async def crear_producto(producto: ProductoCreate) -> ProductoResponse:
    nuevo = await db.producto.create(
        data={
            "titulo": producto.titulo,
            "categoria": producto.categoria,
            "precio": producto.precio,
            "descripcion": producto.descripcion,
        }
    )
    return ProductoResponse(
        id=str(nuevo.id),
        titulo=nuevo.titulo,
        categoria=nuevo.categoria,
        precio=nuevo.precio,
        descripcion=nuevo.descripcion,
    )

async def obtener_productos() -> List[ProductoResponse]:
    productos = await db.producto.find_many()
    return [
        ProductoResponse(
            id=str(item.id),
            titulo=item.titulo,
            categoria=item.categoria,
            precio=item.precio,
            descripcion=item.descripcion,
        )
        for item in productos
    ]

async def obtener_producto_por_id(producto_id: str) -> Optional[ProductoResponse]:
    producto = await db.producto.find_unique(where={"id": producto_id})
    if producto is None:
        return None
    return ProductoResponse(
        id=str(producto.id),
        titulo=producto.titulo,
        categoria=producto.categoria,
        precio=producto.precio,
        descripcion=producto.descripcion,
    )

async def actualizar_producto(producto_id: str, producto: ProductoUpdate) -> Optional[ProductoResponse]:
    existente = await db.producto.find_unique(where={"id": producto_id})
    if existente is None:
        return None

    actualizado = await db.producto.update(
        where={"id": producto_id},
        data={
            "titulo": producto.titulo,
            "categoria": producto.categoria,
            "precio": producto.precio,
            "descripcion": producto.descripcion,
        },
    )

    return ProductoResponse(
        id=str(actualizado.id),
        titulo=actualizado.titulo,
        categoria=actualizado.categoria,
        precio=actualizado.precio,
        descripcion=actualizado.descripcion,
    )

async def eliminar_producto(producto_id: str) -> bool:
    producto = await db.producto.find_unique(where={"id": producto_id})
    if producto is None:
        return False

    await db.producto.delete(where={"id": producto_id})
    return True
