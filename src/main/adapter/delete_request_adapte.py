from typing import Type

from cerberus import Validator
from flask import request as FlaskRequest
from src.errors.validators_errors import SchemaErrors
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.views_interface import ViewInterface


def delete_request_adapter(request: FlaskRequest, callback: Type[ViewInterface]) -> HttpResponse:
    request_validate =  Validator(
        {
            "data": {
                "type": "dict",
                "schema": {
                    "name": {"type": "string", "required": True, "empty": False, "minlength": 3,"maxlength": 255},
                }
            }
        }
    )
    validat = request_validate.validate({"data": request.json})
    if validat is False:
        raise SchemaErrors(request_validate.errors["data"])
        
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        url=request.path
    )
    http_response = callback.handle(http_request)
    return http_response
