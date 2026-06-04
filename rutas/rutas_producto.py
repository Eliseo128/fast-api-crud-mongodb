from typing import List

from fastapi import APIRouter, HTTPException

from esquema.producto_esquema import ProductoCreate, ProductoResponse, ProductoUpdate
from servicios.producto_servicio import (
    crear_producto,
    eliminar_producto,
    obtener_producto_por_id,
    obtener_productos,
    actualizar_producto,
)

router = APIRouter()

@router.get("", response_model=List[ProductoResponse])
async def listar_productos():
    return await obtener_productos()

@router.get("/{producto_id}", response_model=ProductoResponse)
async def obtener_producto(producto_id: str):
    producto = await obtener_producto_por_id(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("", response_model=ProductoResponse, status_code=201)
async def crear_nuevo_producto(producto: ProductoCreate):
    return await crear_producto(producto)

@router.put("/{producto_id}", response_model=ProductoResponse)
async def editar_producto(producto_id: str, producto: ProductoUpdate):
    actualizado = await actualizar_producto(producto_id, producto)
    if actualizado is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return actualizado

@router.delete("/{producto_id}", status_code=204)
async def borrar_producto(producto_id: str):
    exitoso = await eliminar_producto(producto_id)
    if not exitoso:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None
