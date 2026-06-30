from flask import Blueprint
from controllers.compra_controller import (
    listar_compras,
    buscar_compra,
    registrar_compra,
    editar_compra,
    borrar_compra
)

compra_bp = Blueprint("compra", __name__)

@compra_bp.route("/api/compras", methods=["GET"])
def get_compras():
    return listar_compras()

@compra_bp.route("/api/compras/<int:id_compra>", methods=["GET"])
def get_compra(id_compra):
    return buscar_compra(id_compra)

@compra_bp.route("/api/compras", methods=["POST"])
def post_compra():
    return registrar_compra()

@compra_bp.route("/api/compras/<int:id_compra>", methods=["PUT"])
def put_compra(id_compra):
    return editar_compra(id_compra)

@compra_bp.route("/api/compras/<int:id_compra>", methods=["DELETE"])
def delete_compra(id_compra):
    return borrar_compra(id_compra)