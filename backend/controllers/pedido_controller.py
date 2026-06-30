from flask import request
from services.pedido_services import (
    obtener_pedidos,
    obtener_pedido_por_id,
    crear_pedido,
    actualizar_estado_pedido,
    eliminar_pedido
)

def listar_pedidos():
    return obtener_pedidos()

def buscar_pedido(id_pedido):
    return obtener_pedido_por_id(id_pedido)



def registrar_pedido():
    datos = request.get_json()

    if not datos or "productos" not in datos:
        return {
            "estado": "ERROR",
            "mensaje": "Faltan datos: se requiere id_cliente, id_empleado, id_mesa y productos"
        }, 400

    return crear_pedido(
        datos["id_cliente"],
        datos["id_empleado"],
        datos["id_mesa"],
        datos["productos"]
    )


def editar_pedido(id_pedido):
    datos = request.get_json()

    if not datos or "estado" not in datos:
        return {
            "estado": "ERROR",
            "mensaje": "Falta el campo 'estado'"
        }, 400

    return actualizar_estado_pedido(id_pedido, datos["estado"])

def borrar_pedido(id_pedido):
    return eliminar_pedido(id_pedido)