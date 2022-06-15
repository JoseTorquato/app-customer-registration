from typing import Dict, Type

from faker import Faker

fake = Faker()
class UpdateCustomerRegisterControllerSpy:
    def __init__(self) -> None:
        self.data = {} 

    def process(self, data: Dict, db_name: str) -> any:
        self.data = data

        if self.data:
            return fake.name()
        return None  


def test_update():
    update_customer_controller = UpdateCustomerRegisterControllerSpy()
    payload = {
        "id": 1,
        "nome": fake.name(),
        "age": fake.random_number(),
        "district": "Guajuviras",
        "profission": "QA"

    }

    result = update_customer_controller.process(payload, fake.name())

    # Testing input
    assert update_customer_controller.data == payload

    # Testing output
    assert result is not None
