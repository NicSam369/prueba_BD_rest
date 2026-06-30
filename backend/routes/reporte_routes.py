from flask import Blueprint
from controllers.reporte_controller import reporte_categorias

reporte_bp = Blueprint("reporte", __name__)


@reporte_bp.route("/api/reporte/categorias", methods=["GET"])
def get_reporte_categorias():
    return reporte_categorias()
