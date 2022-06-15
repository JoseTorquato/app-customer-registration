from typing import Dict, Type

from faker import Faker


class DeleteCustomerRegisterControllerSpy:
    def __init__(self) -> None:
        self.data = {} 

    def process(self, data: Dict, db_name: str) -> any:
        self.data = data

        if self.data:
            return fake.name()
        return None  

fake = Faker()
def test_delete():
    delete_customer_controller = DeleteCustomerRegisterControllerSpy()
    payload = {
        "nome": fake.name(),
    }

    result = delete_customer_controller.process(payload, fake.name())

    # Testing input
    assert delete_customer_controller.data == payload

    # Testing output
    assert result is not None
