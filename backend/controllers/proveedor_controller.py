from flask import request
from services.proveedor_services import (
    obtener_proveedores,
    obtener_proveedor_por_id,
    crear_proveedor,
    actualizar_proveedor,
    eliminar_proveedor
)

def listar_proveedores():
    return obtener_proveedores()

def buscar_proveedor(id_prvdor):
    return obtener_proveedor_por_id(id_prvdor)



def registrar_proveedor():
    datos = request.get_json()

    return crear_proveedor(
        datos["nombre"],
        datos["ruc"],
        datos.get("telefono"),
        datos["email"],
        datos["id_scrsal"]
    )


def editar_proveedor(id_prvdor):
    datos = request.get_json()

    return actualizar_proveedor(
        id_prvdor,
        datos["nombre"],
        datos["ruc"],
        datos.get("telefono"),
        datos["email"],
        datos["id_scrsal"]
    )

def borrar_proveedor(id_prvdor):
    return eliminar_proveedor(id_prvdor)