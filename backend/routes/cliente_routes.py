from flask import Blueprint
from controllers.cliente_controller import (
    listar_clientes,
    buscar_cliente,
    registrar_cliente,
    editar_cliente,
    borrar_cliente
)

cliente_bp = Blueprint("cliente", __name__)

@cliente_bp.route("/api/clientes", methods=["GET"])
def get_clientes():
    return listar_clientes()

@cliente_bp.route("/api/clientes/<int:id_cliente>", methods=["GET"])
def get_cliente(id_cliente):
    return buscar_cliente(id_cliente)

@cliente_bp.route("/api/clientes", methods=["POST"])
def post_cliente():
    return registrar_cliente()

@cliente_bp.route("/api/clientes/<int:id_cliente>", methods=["PUT"])
def put_cliente(id_cliente):
    return editar_cliente(id_cliente)

@cliente_bp.route("/api/clientes/<int:id_cliente>", methods=["DELETE"])
def delete_cliente(id_cliente):
    return borrar_cliente(id_cliente)