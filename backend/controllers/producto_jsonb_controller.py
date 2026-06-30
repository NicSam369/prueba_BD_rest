from flask import request
from services.producto_jsonb_services import obtener_productos_jsonb


def listar_productos_jsonb():
    filtro = request.args.get("filtro")
    valor = request.args.get("valor")

    resultado = obtener_productos_jsonb(filtro, valor)

    # obtener_productos_jsonb ya devuelve {"data": [...]}, así que no hay
    # que volver a meterlo dentro de otro "data" o queda data.data (doble envoltorio)
    return {
        "estado": "OK",
        "data": resultado["data"]
    }
