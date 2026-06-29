from flask import Blueprint
from controllers.sucursal_controller import (
    listar_sucursales,
    buscar_sucursal,
    registrar_sucursal,
    editar_sucursal,
    borrar_sucursal
)

sucursal_bp = Blueprint("sucursal", __name__)

@sucursal_bp.route("/api/sucursales", methods=["GET"])
def get_sucursales():
    return listar_sucursales()

@sucursal_bp.route("/api/sucursales/<int:id_scrsal>", methods=["GET"])
def get_sucursal(id_scrsal):
    return buscar_sucursal(id_scrsal)

@sucursal_bp.route("/api/sucursales", methods=["POST"])
def post_sucursal():
    return registrar_sucursal()

@sucursal_bp.route("/api/sucursales/<int:id_scrsal>", methods=["PUT"])
def put_sucursal(id_scrsal):
    return editar_sucursal(id_scrsal)

@sucursal_bp.route("/api/sucursales/<int:id_scrsal>", methods=["DELETE"])
def delete_sucursal(id_scrsal):
    return borrar_sucursal(id_scrsal)