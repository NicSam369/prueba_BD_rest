from flask import Blueprint
from controllers.mesa_controller import (
    listar_mesas,
    buscar_mesa,
    registrar_mesa,
    editar_mesa,
    borrar_mesa
)

mesa_bp = Blueprint("mesa", __name__)

@mesa_bp.route("/api/mesas", methods=["GET"])
def get_mesas():
    return listar_mesas()

@mesa_bp.route("/api/mesas/<int:id_mesa>", methods=["GET"])
def get_mesa(id_mesa):
    return buscar_mesa(id_mesa)

@mesa_bp.route("/api/mesas", methods=["POST"])
def post_mesa():
    return registrar_mesa()

@mesa_bp.route("/api/mesas/<int:id_mesa>", methods=["PUT"])
def put_mesa(id_mesa):
    return editar_mesa(id_mesa)

@mesa_bp.route("/api/mesas/<int:id_mesa>", methods=["DELETE"])
def delete_mesa(id_mesa):
    return borrar_mesa(id_mesa)