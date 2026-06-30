from flask import request
from services.compra_services import (
    obtener_compras,
    obtener_compra_por_id,
    crear_compra,
    actualizar_compra,
    eliminar_compra
)

def listar_compras():
    return obtener_compras()

def buscar_compra(id_compra):
    return obtener_compra_por_id(id_compra)


def registrar_compra():
    datos = request.get_json()

    return crear_compra(
        datos["fecha"],
        datos["total"],
        datos["estado"],
        datos["id_scrsal"],
        datos["id_prvdor"]
    )


def editar_compra(id_compra):
    datos = request.get_json()

    return actualizar_compra(
        id_compra,
        datos["fecha"],
        datos["total"],
        datos["estado"],
        datos["id_scrsal"],
        datos["id_prvdor"]
    )


def borrar_compra(id_compra):
    return eliminar_compra(id_compra)