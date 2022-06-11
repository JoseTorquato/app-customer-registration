from typing import Dict, Type

from src.models.interfaces.repository_interface import RepositoryInterface


class CreateCustomerRegisterController:
    def __init__(self, repository: Type[RepositoryInterface]) -> None:
        self.__repository = repository 

    def create_person(self, data: Dict, db_name: str) -> any:
        data["id"] = len(self.__repository.select(db_name)) + 1
        return self.__repository.create(data, db_name)  
