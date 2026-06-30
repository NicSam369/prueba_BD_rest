from flask import request
from services.empleado_services import (
    obtener_empleados,
    obtener_empleado_por_id,
    crear_empleado,
    actualizar_empleado,
    eliminar_empleado
)

def listar_empleados():
    return obtener_empleados()

def buscar_empleado(id_empleado):
    return obtener_empleado_por_id(id_empleado)



def registrar_empleado():
    datos = request.get_json()

    return crear_empleado(
        datos["nombre"],
        datos["apellido"],
        datos["dni"],
        datos["email"],
        datos.get("telefono"),
        datos["rol"],
        datos["turno"],
        datos["id_scrsal"]
    )


def editar_empleado(id_empleado):
    datos = request.get_json()

    return actualizar_empleado(
        id_empleado,
        datos["nombre"],
        datos["apellido"],
        datos["dni"],
        datos["email"],
        datos.get("telefono"),
        datos["rol"],
        datos["turno"],
        datos["id_scrsal"]
    )

def borrar_empleado(id_empleado):
    return eliminar_empleado(id_empleado)