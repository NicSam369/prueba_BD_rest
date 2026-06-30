from flask import request
from services.mesa_services import (
    obtener_mesas,
    obtener_mesa_por_id,
    crear_mesa,
    actualizar_mesa,
    eliminar_mesa
)

def listar_mesas():
    return obtener_mesas()

def buscar_mesa(id_mesa):
    return obtener_mesa_por_id(id_mesa)



def registrar_mesa():
    datos = request.get_json()

    return crear_mesa(
        datos["id_scrsal"],
        datos["numero"],
        datos["capacidad"],
        datos["estado"]
    )


def editar_mesa(id_mesa):
    datos = request.get_json()

    return actualizar_mesa(
        id_mesa,
        datos["id_scrsal"],
        datos["numero"],
        datos["capacidad"],
        datos["estado"]
    )

def borrar_mesa(id_mesa):
    return eliminar_mesa(id_mesa)