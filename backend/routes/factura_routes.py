from flask import Blueprint
from controllers.factura_controller import (
    listar_facturas,
    buscar_factura,
    registrar_factura,
    editar_factura,
    borrar_factura
)

factura_bp = Blueprint("factura", __name__)

@factura_bp.route("/api/facturas", methods=["GET"])
def get_facturas():
    return listar_facturas()

@factura_bp.route("/api/facturas/<int:id_factura>", methods=["GET"])
def get_factura(id_factura):
    return buscar_factura(id_factura)

@factura_bp.route("/api/facturas", methods=["POST"])
def post_factura():
    return registrar_factura()

@factura_bp.route("/api/facturas/<int:id_factura>", methods=["PUT"])
def put_factura(id_factura):
    return editar_factura(id_factura)

@factura_bp.route("/api/facturas/<int:id_factura>", methods=["DELETE"])
def delete_factura(id_factura):
    return borrar_factura(id_factura)