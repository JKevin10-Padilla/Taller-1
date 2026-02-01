from pydantic import BaseModel
from typing import Optional

class News(BaseModel):
    titulo: str
    descripcion: Optional[str]
    fuente: str
    autor: Optional[str]
    url: str
    imagen: Optional[str]
    fecha: str
