from flask import request
from services.cliente_services import (
    obtener_clientes,
    obtener_cliente_por_id,
    crear_cliente,
    actualizar_cliente,
    eliminar_cliente
)

def listar_clientes():
    return obtener_clientes()

def buscar_cliente(id_cliente):
    return obtener_cliente_por_id(id_cliente)



def registrar_cliente():
    datos = request.get_json()

    return crear_cliente(
        datos["nombre"],
        datos["apellido"],
        datos["email"],
        datos["dni"],
        datos.get("telefono")
    )


def editar_cliente(id_cliente):
    datos = request.get_json()

    return actualizar_cliente(
        id_cliente,
        datos["nombre"],
        datos["apellido"],
        datos["email"],
        datos["dni"],
        datos.get("telefono")
    )

def borrar_cliente(id_cliente):
    return eliminar_cliente(id_cliente)