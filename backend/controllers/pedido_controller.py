from flask import request
from services.pedido_services import (
    obtener_pedidos,
    obtener_pedido_por_id,
    crear_pedido,
    actualizar_pedido,
    eliminar_pedido
)

def listar_pedidos():
    return obtener_pedidos()

def buscar_pedido(id_pedido):
    return obtener_pedido_por_id(id_pedido)



def registrar_pedido():
    datos = request.get_json()

    return crear_pedido(
        datos["id_cliente"],
        datos["id_empleado"],
        datos["id_mesa"],
        datos["estado"],
        datos["total"]
    )


def editar_pedido(id_pedido):
    datos = request.get_json()

    return actualizar_pedido(
        id_pedido,
        datos["id_cliente"],
        datos["id_empleado"],
        datos["id_mesa"],
        datos["fecha_hora"],
        datos["estado"],
        datos["total"]
    )

def borrar_pedido(id_pedido):
    return eliminar_pedido(id_pedido)