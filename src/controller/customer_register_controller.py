from typing import List, Type

from src.controller.interface.customer_register_interface import \
    CustomerRegisterInterface
from src.models.interfaces.repository_interface import RepositoryInterface


class CustomerRegisterController(CustomerRegisterInterface):
    def __init__(self, repository: Type[RepositoryInterface]) -> None:
        self.__repository = repository        

    def search_person(self, data, db_name) -> any:
        return self.__repository.search_by_name(data["name"], db_name)  

    def create_person(self, data, db_name) -> any:
        data["id"] = len(self.__repository.select(db_name)) + 1
        return self.__repository.create(data, db_name)   

    def update_person(self, data, db_name) -> any:
        return self.__repository.update(data, db_name)       

    def delete_person(self, data, db_name) -> any:
        return self.__repository.delete(data, db_name)     

    def get_person(self, db_name) -> List:
        return self.__repository.select(db_name)
