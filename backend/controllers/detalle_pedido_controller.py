from flask import request
from services.detalle_pedido_services import (
    obtener_detalles_pedido,
    obtener_detalle_por_id,
    crear_detalle,
    actualizar_detalle,
    eliminar_detalle
)

def listar_detalles():
    return obtener_detalles_pedido()

def buscar_detalle(id_detalle):
    return obtener_detalle_por_id(id_detalle)

def registrar_detalle():
    datos = request.get_json()

    return crear_detalle(
        datos["id_pedido"],
        datos["id_producto"],
        datos["cantidad"],
        datos["precio_unitario"],
        datos["subtotal"]
    )

def editar_detalle(id_detalle):
    datos = request.get_json()

    return actualizar_detalle(
        id_detalle,
        datos["id_pedido"],
        datos["id_producto"],
        datos["cantidad"],
        datos["precio_unitario"],
        datos["subtotal"]
    )

def borrar_detalle(id_detalle):
    return eliminar_detalle(id_detalle)