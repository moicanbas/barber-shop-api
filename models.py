from dataclasses import dataclass


@dataclass
class ReservaModel:
    nombre: str
    fecha: str
    hora: str
    servicio: str
