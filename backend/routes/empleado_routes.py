from flask import Blueprint
from controllers.empleado_controller import (
    listar_empleados,
    buscar_empleado,
    registrar_empleado,
    editar_empleado,
    borrar_empleado
)

empleado_bp = Blueprint("empleado", __name__)

@empleado_bp.route("/api/empleados", methods=["GET"])
def get_empleados():
    return listar_empleados()

@empleado_bp.route("/api/empleados/<int:id_empleado>", methods=["GET"])
def get_empleado(id_empleado):
    return buscar_empleado(id_empleado)

@empleado_bp.route("/api/empleados", methods=["POST"])
def post_empleado():
    return registrar_empleado()

@empleado_bp.route("/api/empleados/<int:id_empleado>", methods=["PUT"])
def put_empleado(id_empleado):
    return editar_empleado(id_empleado)

@empleado_bp.route("/api/empleados/<int:id_empleado>", methods=["DELETE"])
def delete_empleado(id_empleado):
    return borrar_empleado(id_empleado)