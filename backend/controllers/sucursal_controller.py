from flask import request
from services.sucursal_services import (
    obtener_sucursales,
    obtener_sucursal_por_id,
    crear_sucursal,
    actualizar_sucursal,
    eliminar_sucursal
)

def listar_sucursales():
    return obtener_sucursales()

def buscar_sucursal(id_scrsal):
    return obtener_sucursal_por_id(id_scrsal)



def registrar_sucursal():
    datos = request.get_json()

    return crear_sucursal(
        datos["nombre"],
        datos["direccion"],
        datos["ciudad"],
        datos.get("telefono")
    )


def editar_sucursal(id_scrsal):
    datos = request.get_json()

    return actualizar_sucursal(
        id_scrsal,
        datos["nombre"],
        datos["direccion"],
        datos["ciudad"],
        datos.get("telefono")
    )

def borrar_sucursal(id_scrsal):
    return eliminar_sucursal(id_scrsal)