from typing import Dict, Type

from src.models.interfaces.repository_interface import RepositoryInterface


class UpdateCustomerRegisterController:
    def __init__(self, repository: Type[RepositoryInterface]) -> Dict:
        self.__repository = repository

    def process(self, data: Dict, db_name: str) -> Dict:
        return self.__repository.update(data, db_name)
