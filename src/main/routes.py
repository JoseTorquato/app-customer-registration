from flask import Blueprint, jsonify, request

customer_registration_routes_bp = Blueprint("api_routes", __name__)

from src.main.adapter.request_adapter import request_adapter
from src.main.composer.customer_register_composer import \
    customer_registration_composer


@customer_registration_routes_bp.route("/persons", methods=["GET"])
def persons():
    http_response = request_adapter(request, customer_registration_composer())
    return jsonify(http_response.body), http_response.status_code


@customer_registration_routes_bp.route("/persons/create", methods=["POST"])
def create():
    http_response = request_adapter(request, customer_registration_composer())
    return jsonify(http_response.body), http_response.status_code


@customer_registration_routes_bp.route("/persons/update", methods=["PUT"])
def update():
    http_response = request_adapter(request, customer_registration_composer())
    return jsonify(http_response.body), http_response.status_code
