from pydantic import BaseModel, Field
from typing import Optional


class Reserva(BaseModel):
    nombre: str = Field(..., example="Juan Pérez")
    fecha: str = Field(..., example="17/04/2025")
    hora: str = Field(..., example="14:30")
    servicio: str = Field(..., example="corte")
