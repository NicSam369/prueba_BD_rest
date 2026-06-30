from flask import request
from services.promocion_services import (
    obtener_promociones,
    obtener_promocion_por_id,
    crear_promocion,
    actualizar_promocion,
    eliminar_promocion
)

def listar_promociones():
    return obtener_promociones()

def buscar_promocion(id_promocion):
    return obtener_promocion_por_id(id_promocion)


def registrar_promocion():
    datos = request.get_json()

    return crear_promocion(
        datos["nombre"],
        datos["descuento_pct"],
        datos["fecha_inicio"],
        datos["fecha_fin"],
        datos["id_scrsal"]
    )


def editar_promocion(id_promocion):
    datos = request.get_json()

    return actualizar_promocion(
        id_promocion,
        datos["nombre"],
        datos["descuento_pct"],
        datos["fecha_inicio"],
        datos["fecha_fin"],
        datos["id_scrsal"]
    )


def borrar_promocion(id_promocion):
    return eliminar_promocion(id_promocion)