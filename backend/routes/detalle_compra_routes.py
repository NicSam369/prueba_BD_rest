from flask import Blueprint
from controllers.detalle_compra_controller import (
    listar_detalles_compra,
    buscar_detalle_compra,
    registrar_detalle_compra,
    editar_detalle_compra,
    borrar_detalle_compra
)

detalle_compra_bp = Blueprint("detalle_compra", __name__)

@detalle_compra_bp.route("/api/detalles_compra", methods=["GET"])
def get_detalles_compra():
    return listar_detalles_compra()

@detalle_compra_bp.route("/api/detalles_compra/<int:id_dtlle_compra>", methods=["GET"])
def get_detalle_compra(id_dtlle_compra):
    return buscar_detalle_compra(id_dtlle_compra)

@detalle_compra_bp.route("/api/detalles_compra", methods=["POST"])
def post_detalle_compra():
    return registrar_detalle_compra()

@detalle_compra_bp.route("/api/detalles_compra/<int:id_dtlle_compra>", methods=["PUT"])
def put_detalle_compra(id_dtlle_compra):
    return editar_detalle_compra(id_dtlle_compra)

@detalle_compra_bp.route("/api/detalles_compra/<int:id_dtlle_compra>", methods=["DELETE"])
def delete_detalle_compra(id_dtlle_compra):
    return borrar_detalle_compra(id_dtlle_compra)