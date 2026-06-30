from flask import Blueprint
from controllers.producto_jsonb_controller import listar_productos_jsonb

producto_jsonb_bp = Blueprint("producto_jsonb", __name__)


@producto_jsonb_bp.route("/api/productos/jsonb", methods=["GET"])
def get_productos_jsonb():
    return listar_productos_jsonb()
