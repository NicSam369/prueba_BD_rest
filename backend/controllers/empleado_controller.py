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

    resultado = crear_empleado(
        datos["nombre"],
        datos["apellido"],
        datos["dni"],
        datos["email"],
        datos.get("telefono"),
        datos["rol"],
        datos["turno"],
        datos["id_scrsal"]
    )

    if resultado.get("estado") == "ERROR":
        return resultado, 400
    return resultado


def editar_empleado(id_empleado):
    datos = request.get_json()

    resultado = actualizar_empleado(
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

    if resultado.get("estado") == "ERROR":
        return resultado, 400
    return resultado

def borrar_empleado(id_empleado):
    resultado = eliminar_empleado(id_empleado)
    if resultado.get("estado") == "ERROR":
        return resultado, 400
    return resultado