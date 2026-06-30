from flask import request
from services.reserva_services import (
    obtener_reservas,
    obtener_reserva_por_id,
    crear_reserva,
    actualizar_reserva,
    eliminar_reserva
)

def listar_reservas():
    return obtener_reservas()

def buscar_reserva(id_reserva):
    return obtener_reserva_por_id(id_reserva)


def registrar_reserva():
    datos = request.get_json()

    return crear_reserva(
        datos["fecha_reserva"],
        datos["hora"],
        datos["num_personas"],
        datos["estado"],
        datos["id_cliente"],
        datos["id_mesa"],
        datos["id_scrsal"]
    )


def editar_reserva(id_reserva):
    datos = request.get_json()

    return actualizar_reserva(
        id_reserva,
        datos["fecha_reserva"],
        datos["hora"],
        datos["num_personas"],
        datos["estado"],
        datos["id_cliente"],
        datos["id_mesa"],
        datos["id_scrsal"]
    )


def borrar_reserva(id_reserva):
    return eliminar_reserva(id_reserva)