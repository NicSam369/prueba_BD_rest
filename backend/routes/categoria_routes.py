from flask import Blueprint
from controllers.categoria_controller import (
    listar_categorias,
    buscar_categoria,
    editar_categoria,
    registrar_categoria,
    borrar_categoria
)

categoria_bp = Blueprint("categoria", __name__)

@categoria_bp.route("/api/categorias", methods=["GET"])
def get_categorias():
    return listar_categorias()

@categoria_bp.route("/api/categorias/<int:id_categoria>", methods=["GET"])
def get_categoria(id_categoria):
    return buscar_categoria(id_categoria)

@categoria_bp.route("/api/categorias", methods=["POST"])
def post_categoria():
    return registrar_categoria()

@categoria_bp.route("/api/categorias/<int:id_categoria>", methods=["PUT"])
def put_categoria(id_categoria):
    return editar_categoria(id_categoria)

@categoria_bp.route("/api/categorias/<int:id_categoria>", methods=["DELETE"])
def delete_categoria(id_categoria):
    return borrar_categoria(id_categoria)