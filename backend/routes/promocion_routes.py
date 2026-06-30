from flask import Blueprint
from controllers.promocion_controller import (
    listar_promociones,
    buscar_promocion,
    registrar_promocion,
    editar_promocion,
    borrar_promocion
)

promocion_bp = Blueprint("promocion", __name__)

@promocion_bp.route("/api/promociones", methods=["GET"])
def get_promociones():
    return listar_promociones()

@promocion_bp.route("/api/promociones/<int:id_promocion>", methods=["GET"])
def get_promocion(id_promocion):
    return buscar_promocion(id_promocion)

@promocion_bp.route("/api/promociones", methods=["POST"])
def post_promocion():
    return registrar_promocion()

@promocion_bp.route("/api/promociones/<int:id_promocion>", methods=["PUT"])
def put_promocion(id_promocion):
    return editar_promocion(id_promocion)

@promocion_bp.route("/api/promociones/<int:id_promocion>", methods=["DELETE"])
def delete_promocion(id_promocion):
    return borrar_promocion(id_promocion)