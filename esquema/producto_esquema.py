from pydantic import BaseModel

class ProductoBase(BaseModel):
    titulo: str
    categoria: str
    precio: float
    descripcion: str

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: str

    model_config = {
        "from_attributes": True,
    }
