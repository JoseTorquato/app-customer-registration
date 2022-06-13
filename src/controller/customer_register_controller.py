from typing import List, Type

from src.controller.interface.customer_register_interface import \
    CustomerRegisterInterface
from src.models.interfaces.repository_interface import RepositoryInterface


class CustomerRegisterController:
    def __init__(self, repository: Type[RepositoryInterface]) -> None:
        self.__repository = repository        

    def search_person(self, data, db_name) -> any:
        return self.__repository.search_by_name(data["name"], db_name)  

    def get_person(self, db_name) -> List:
        return self.__repository.select(db_name)
