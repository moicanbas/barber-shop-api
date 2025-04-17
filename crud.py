import csv
import os
from typing import List
from models import ReservaModel

ARCHIVO_RESERVAS = 'reservas.csv'


def leer_reservas() -> List[ReservaModel]:
    if not os.path.exists(ARCHIVO_RESERVAS):
        return []
    with open(ARCHIVO_RESERVAS, mode='r', newline='') as archivo:
        reader = csv.reader(archivo)
        return [ReservaModel(*row) for row in reader]


def escribir_reserva(reserva: ReservaModel):
    with open(ARCHIVO_RESERVAS, mode='a', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([reserva.nombre, reserva.fecha, reserva.hora, reserva.servicio])


def eliminar_reserva(nombre: str, fecha: str):
    reservas = leer_reservas()
    nuevas_reservas = [r for r in reservas if not (r.nombre == nombre and r.fecha == fecha)]
    with open(ARCHIVO_RESERVAS, mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        for r in nuevas_reservas:
            writer.writerow([r.nombre, r.fecha, r.hora, r.servicio])
    return len(reservas) != len(nuevas_reservas)
