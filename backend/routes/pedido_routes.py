from flask import Blueprint
from controllers.pedido_controller import (
    listar_pedidos,
    buscar_pedido,
    registrar_pedido,
    editar_pedido,
    borrar_pedido
)

pedido_bp = Blueprint("pedido", __name__)

@pedido_bp.route("/api/pedidos", methods=["GET"])
def get_pedidos():
    return listar_pedidos()

@pedido_bp.route("/api/pedidos/<int:id_pedido>", methods=["GET"])
def get_pedido(id_pedido):
    return buscar_pedido(id_pedido)

@pedido_bp.route("/api/pedidos", methods=["POST"])
def post_pedido():
    return registrar_pedido()

@pedido_bp.route("/api/pedidos/<int:id_pedido>", methods=["PUT"])
def put_pedido(id_pedido):
    return editar_pedido(id_pedido)

@pedido_bp.route("/api/pedidos/<int:id_pedido>", methods=["DELETE"])
def delete_pedido(id_pedido):
    return borrar_pedido(id_pedido)