from flask import Blueprint
from controllers.detalle_pedido_controller import (
    listar_detalles,
    buscar_detalle,
    registrar_detalle,
    editar_detalle,
    borrar_detalle
)

detalle_pedido_bp = Blueprint("detalle_pedido", __name__)

@detalle_pedido_bp.route("/api/detalles_pedido", methods=["GET"])
def get_detalles():
    return listar_detalles()

@detalle_pedido_bp.route("/api/detalles_pedido/<int:id_detalle>", methods=["GET"])
def get_detalle(id_detalle):
    return buscar_detalle(id_detalle)

@detalle_pedido_bp.route("/api/detalles_pedido", methods=["POST"])
def post_detalle():
    return registrar_detalle()

@detalle_pedido_bp.route("/api/detalles_pedido/<int:id_detalle>", methods=["PUT"])
def put_detalle(id_detalle):
    return editar_detalle(id_detalle)

@detalle_pedido_bp.route("/api/detalles_pedido/<int:id_detalle>", methods=["DELETE"])
def delete_detalle(id_detalle):
    return borrar_detalle(id_detalle)