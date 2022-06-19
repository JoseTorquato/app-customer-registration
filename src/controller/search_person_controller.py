from typing import Dict, Type

from src.models.interfaces.repository_interface import RepositoryInterface


class SearchCustomerRegisterController:
    def __init__(self, repository: Type[RepositoryInterface]) -> None:
        self.__repository = repository 

    def process(self, data: Dict, db_name: str) -> any:
        return self.__repository.search_by_name(data["name"], db_name)
