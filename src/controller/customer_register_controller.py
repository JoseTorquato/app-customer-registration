from typing import List, Type

from src.controller.interface.customer_register_interface import \
    CustomerRegisterInterface
from src.models.interfaces.repository_interface import RepositoryInterface


class CustomerRegisterController(CustomerRegisterInterface):
    def __init__(self, repository: Type[RepositoryInterface]) -> None:
        self.__repository = repository        

    def search_person(self, data) -> any:
        print(data)
        return self.__repository.search_by_name(data["name"])  

    def create_person(self, data) -> any:
        data["id"] = len(self.__repository.select()) + 1
        return self.__repository.create(data)   

    def update_person(self, data) -> any:
        return self.__repository.update(data)       

    def delete_person(self, data) -> any:
        return self.__repository.delete(data)     

    def get_person(self) -> List:
        return self.__repository.select()
