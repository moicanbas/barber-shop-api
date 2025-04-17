from fastapi import FastAPI, HTTPException, Query
from schemas import Reserva
from crud import leer_reservas, escribir_reserva, eliminar_reserva
from models import ReservaModel
from utils import validar_formato_fecha, validar_formato_hora
from fastapi.responses import FileResponse
from typing import List

app = FastAPI(title="API Barbería ✂️")


@app.get("/reservas", response_model=List[Reserva])
def obtener_reservas(fecha: str = Query(None, example="17/04/2025")):
    reservas = leer_reservas()
    if fecha:
        return [r for r in reservas if r.fecha == fecha]
    return reservas


@app.post("/reservas")
def crear_reserva(reserva: Reserva):
    if not validar_formato_fecha(reserva.fecha) or not validar_formato_hora(reserva.hora):
        raise HTTPException(status_code=400, detail="Formato de fecha u hora inválido.")
    
    reservas = leer_reservas()
    for r in reservas:
        if r.nombre == reserva.nombre and r.fecha == reserva.fecha and r.hora == reserva.hora:
            raise HTTPException(status_code=409, detail="Ya existe una reserva para ese cliente en ese horario.")
    
    escribir_reserva(ReservaModel(**reserva.dict()))
    return {"message": "✅ Reserva registrada con éxito"}


@app.delete("/reservas")
def borrar_reserva(nombre: str, fecha: str):
    resultado = eliminar_reserva(nombre, fecha)
    if resultado:
        return {"message": "🗑️ Reserva eliminada correctamente"}
    else:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")


@app.get("/exportar")
def exportar_reservas():
    return FileResponse(path='reservas.csv', filename="reservas.csv", media_type='text/csv')
