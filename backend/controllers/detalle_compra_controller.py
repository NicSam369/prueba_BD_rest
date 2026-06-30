from flask import request
from services.detalle_compra_services import (
    obtener_detalles_compra,
    obtener_detalle_compra_por_id,
    crear_detalle_compra,
    actualizar_detalle_compra,
    eliminar_detalle_compra
)

def listar_detalles_compra():
    return obtener_detalles_compra()

def buscar_detalle_compra(id_dtlle_compra):
    return obtener_detalle_compra_por_id(id_dtlle_compra)


def registrar_detalle_compra():
    datos = request.get_json()

    return crear_detalle_compra(
        datos["cantidad"],
        datos["subtotal"],
        datos["precio_unitario"],
        datos["id_producto"],
        datos["id_compra"]
    )


def editar_detalle_compra(id_dtlle_compra):
    datos = request.get_json()

    return actualizar_detalle_compra(
        id_dtlle_compra,
        datos["cantidad"],
        datos["subtotal"],
        datos["precio_unitario"],
        datos["id_producto"],
        datos["id_compra"]
    )


def borrar_detalle_compra(id_dtlle_compra):
    return eliminar_detalle_compra(id_dtlle_compra)