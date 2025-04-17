import re


def validar_formato_fecha(fecha: str) -> bool:
    return bool(re.match(r"\d{2}/\d{2}/\d{4}", fecha))


def validar_formato_hora(hora: str) -> bool:
    return bool(re.match(r"\d{2}:\d{2}", hora))
