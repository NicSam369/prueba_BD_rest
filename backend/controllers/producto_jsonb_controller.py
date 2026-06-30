from flask import request
from services.producto_jsonb_services import obtener_productos_jsonb


def listar_productos_jsonb():
    filtro = request.args.get("filtro")
    valor = request.args.get("valor")

    datos = obtener_productos_jsonb(filtro, valor)

    return {
        "estado": "OK",
        "data": datos
    }
