from flask import request
from services.factura_services import (
    obtener_facturas,
    obtener_factura_por_id,
    crear_factura,
    actualizar_factura,
    eliminar_factura
)

def listar_facturas():
    return obtener_facturas()

def buscar_factura(id_factura):
    return obtener_factura_por_id(id_factura)


def registrar_factura():
    datos = request.get_json()

    return crear_factura(
        datos["numero"],
        datos["fecha_emision"],
        datos["monto_total"],
        datos["id_pago"]
    )


def editar_factura(id_factura):
    datos = request.get_json()

    return actualizar_factura(
        id_factura,
        datos["numero"],
        datos["fecha_emision"],
        datos["monto_total"],
        datos["id_pago"]
    )


def borrar_factura(id_factura):
    return eliminar_factura(id_factura)