from typing import Type

from src.controller.interface.customer_register_interface import \
    CustomerRegisterInterface

from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.views_interface import ViewInterface


class CustomerRegisterView(ViewInterface):
    def __init__(self, controller: Type[CustomerRegisterInterface]) -> None:
        self.__controller = controller
    
    def handle(self, http_request: Type[HttpRequest]) -> Type[HttpResponse]:
        try:
            if http_request.body:
                response = self.__controller.process(http_request.body, "customer_registration.db")
            else:
                response = self.__controller.process("customer_registration.db")
                
            return HttpResponse(status_code=200, body={ "response": response })
        except Exception as exception:
            return HttpResponse(status_code=500, body=exception.error_json())
