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
        # try:
            if http_request.url == "/persons":
                response = self.__controller.get_person()
            elif http_request.url == "/persons/create":
                response = self.__controller.create_person(http_request.body)
            elif http_request.url == "/persons/update":
                response = self.__controller.update_person(http_request.body)
            else:
                response = None
                
            return HttpResponse(status_code=200, body={ "response": response })
        # except Exception as exception:
        #     return HttpResponse(status_code=500, body={ "error": str(exception) })
