from flask import Blueprint
from controllers.producto_controller import (
    listar_productos,
    buscar_producto,
    registrar_producto,
    editar_producto,
    borrar_producto
)

producto_bp = Blueprint("producto", __name__)

@producto_bp.route("/api/productos", methods=["GET"])
def get_productos():
    return listar_productos()

@producto_bp.route("/api/productos/<int:id_producto>", methods=["GET"])
def get_producto(id_producto):
    return buscar_producto(id_producto)

@producto_bp.route("/api/productos", methods=["POST"])
def post_producto():
    return registrar_producto()

@producto_bp.route("/api/productos/<int:id_producto>", methods=["PUT"])
def put_producto(id_producto):
    return editar_producto(id_producto)

@producto_bp.route("/api/productos/<int:id_producto>", methods=["DELETE"])
def delete_producto(id_producto):
    return borrar_producto(id_producto)