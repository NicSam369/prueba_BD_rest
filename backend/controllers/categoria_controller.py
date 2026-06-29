from flask import request
from services.categoria_services import (
    obtener_categorias,
    obtener_categoria_por_id,
    crear_categoria,
    actualizar_categoria,
    eliminar_categoria
)

def listar_categorias():
    return obtener_categorias()

def buscar_categoria(id_categoria):
    return obtener_categoria_por_id(id_categoria)



def registrar_categoria():
    datos = request.get_json()

    return crear_categoria(
        datos["nombre"],
        datos["descripcion"]
    )


def editar_categoria(id_categoria):
    datos = request.get_json()

    return actualizar_categoria(
        id_categoria,
        datos["nombre"],
        datos["descripcion"]
    )

def borrar_categoria(id_categoria):
    return eliminar_categoria(id_categoria)