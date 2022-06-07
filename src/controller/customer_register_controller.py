from typing import List, Type

from src.controller.interface.customer_register_interface import \
    CustomerRegisterInterface
from src.models.interfaces.repository_interface import RepositoryInterface


class CustomerRegisterController(CustomerRegisterInterface):
    def __init__(self, repository: Type[RepositoryInterface]) -> None:
        self.__repository = repository        

    def create_person(self) -> any:
        return self.__repository.create()     

    def get_person(self) -> List:
        return self.__repository.select()
