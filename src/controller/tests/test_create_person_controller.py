from typing import Dict, Type

from faker import Faker
from src.models.interfaces.repository_interface import RepositoryInterface
from src.models.repository import Repository

fake = Faker()
class CreateCustomerRegisterControllerSpy:
    def __init__(self) -> None:
        self.data = {}

    def process(self, data: Dict, db_name: str) -> any:
        data["id"] = 1
        self.data = data

        if self.data:
            return fake.name()
        return None

def test_create():
    create_customer_controller = CreateCustomerRegisterControllerSpy()
    payload = {
        "nome": fake.name(),
        "age": fake.random_number()
    }

    result = create_customer_controller.process(payload, fake.name())

    # Testing input
    assert create_customer_controller.data == payload

    # Testing output
    assert result is not None
