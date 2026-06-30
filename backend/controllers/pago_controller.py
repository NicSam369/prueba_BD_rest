from flask import request
from services.pago_services import (
    obtener_pagos,
    obtener_pago_por_id,
    crear_pago,
    actualizar_pago,
    eliminar_pago
)

def listar_pagos():
    return obtener_pagos()

def buscar_pago(id_pago):
    return obtener_pago_por_id(id_pago)


def registrar_pago():
    datos = request.get_json()

    return crear_pago(
        datos["monto"],
        datos["metodo"],
        datos["fcha_pago"],
        datos["estado"],
        datos["id_pedido"]
    )


def editar_pago(id_pago):
    datos = request.get_json()

    return actualizar_pago(
        id_pago,
        datos["monto"],
        datos["metodo"],
        datos["fcha_pago"],
        datos["estado"],
        datos["id_pedido"]
    )


def borrar_pago(id_pago):
    return eliminar_pago(id_pago)