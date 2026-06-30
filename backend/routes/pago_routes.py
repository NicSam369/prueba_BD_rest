from flask import Blueprint
from controllers.pago_controller import (
    listar_pagos,
    buscar_pago,
    registrar_pago,
    editar_pago,
    borrar_pago
)

pago_bp = Blueprint("pago", __name__)

@pago_bp.route("/api/pagos", methods=["GET"])
def get_pagos():
    return listar_pagos()

@pago_bp.route("/api/pagos/<int:id_pago>", methods=["GET"])
def get_pago(id_pago):
    return buscar_pago(id_pago)

@pago_bp.route("/api/pagos", methods=["POST"])
def post_pago():
    return registrar_pago()

@pago_bp.route("/api/pagos/<int:id_pago>", methods=["PUT"])
def put_pago(id_pago):
    return editar_pago(id_pago)

@pago_bp.route("/api/pagos/<int:id_pago>", methods=["DELETE"])
def delete_pago(id_pago):
    return borrar_pago(id_pago)