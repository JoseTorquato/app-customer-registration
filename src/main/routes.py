from typing import Type

from flask import Blueprint, jsonify, request
from src.main.adapter.create_request_adapter import create_request_adapter
from src.main.adapter.delete_request_adapte import delete_request_adapter
from src.main.adapter.update_request_adapte import update_request_adapter
from src.main.composer.customer_register_composer import \
    customer_registration_composer
from src.main.composer.delete_person_composer import \
    delete_customer_registration_composer
from src.main.composer.update_person_composer import \
    update_customer_registration_composer

customer_registration_routes_bp = Blueprint("api_routes", __name__)

from src.main.adapter.request_adapter import request_adapter
from src.main.composer.create_person_composer import \
    create_customer_registration_composer


@customer_registration_routes_bp.route("/person/search", methods=["POST"])
def person():
    http_response = request_adapter(request, customer_registration_composer())
    return jsonify(http_response.body), http_response.status_code

@customer_registration_routes_bp.route("/persons", methods=["GET"])
def persons():
    http_response = request_adapter(request, customer_registration_composer())
    return jsonify(http_response.body), http_response.status_code

@customer_registration_routes_bp.route("/person/create", methods=["POST"])
def create():
    try:
        http_response = create_request_adapter(request, create_customer_registration_composer())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        return exception.error_json()
        
@customer_registration_routes_bp.route("/person/update", methods=["PUT"])
def update():
    try:
        http_response = update_request_adapter(request, update_customer_registration_composer())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        return exception.error_json()

@customer_registration_routes_bp.route("/person/delete", methods=["DELETE"])
def delete():
    try:
        http_response = delete_request_adapter(request, delete_customer_registration_composer())
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        return exception.error_json()
