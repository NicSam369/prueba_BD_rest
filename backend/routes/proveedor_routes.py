from flask import Blueprint
from controllers.proveedor_controller import (
    listar_proveedores,
    buscar_proveedor,
    registrar_proveedor,
    editar_proveedor,
    borrar_proveedor
)

proveedor_bp = Blueprint("proveedor", __name__)

@proveedor_bp.route("/api/proveedores", methods=["GET"])
def get_proveedores():
    return listar_proveedores()

@proveedor_bp.route("/api/proveedores/<int:id_prvdor>", methods=["GET"])
def get_proveedor(id_prvdor):
    return buscar_proveedor(id_prvdor)

@proveedor_bp.route("/api/proveedores", methods=["POST"])
def post_proveedor():
    return registrar_proveedor()

@proveedor_bp.route("/api/proveedores/<int:id_prvdor>", methods=["PUT"])
def put_proveedor(id_prvdor):
    return editar_proveedor(id_prvdor)

@proveedor_bp.route("/api/proveedores/<int:id_prvdor>", methods=["DELETE"])
def delete_proveedor(id_prvdor):
    return borrar_proveedor(id_prvdor)