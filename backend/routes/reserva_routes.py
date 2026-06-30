from flask import Blueprint
from controllers.reserva_controller import (
    listar_reservas,
    buscar_reserva,
    registrar_reserva,
    editar_reserva,
    borrar_reserva
)

reserva_bp = Blueprint("reserva", __name__)

@reserva_bp.route("/api/reservas", methods=["GET"])
def get_reservas():
    return listar_reservas()

@reserva_bp.route("/api/reservas/<int:id_reserva>", methods=["GET"])
def get_reserva(id_reserva):
    return buscar_reserva(id_reserva)

@reserva_bp.route("/api/reservas", methods=["POST"])
def post_reserva():
    return registrar_reserva()

@reserva_bp.route("/api/reservas/<int:id_reserva>", methods=["PUT"])
def put_reserva(id_reserva):
    return editar_reserva(id_reserva)

@reserva_bp.route("/api/reservas/<int:id_reserva>", methods=["DELETE"])
def delete_reserva(id_reserva):
    return borrar_reserva(id_reserva)