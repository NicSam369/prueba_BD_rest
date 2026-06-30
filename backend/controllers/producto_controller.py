from flask import request
from services.producto_services import (
    obtener_productos,
    obtener_producto_por_id,
    crear_producto,
    actualizar_producto,
    eliminar_producto
)

def listar_productos():
    return obtener_productos()

def buscar_producto(id_producto):
    return obtener_producto_por_id(id_producto)



def registrar_producto():
    datos = request.get_json()

    return crear_producto(
        datos["nombre"],
        datos["descripcion"],
        datos["precio"],
        datos["stock"],
        datos["id_categoria"]
    )


def editar_producto(id_producto):
    datos = request.get_json()

    return actualizar_producto(
        id_producto,
        datos["nombre"],
        datos["descripcion"],
        datos["precio"],
        datos["stock"],
        datos["id_categoria"]
    )

def borrar_producto(id_producto):
    return eliminar_producto(id_producto)