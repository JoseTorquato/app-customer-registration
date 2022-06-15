from typing import Dict

from faker import Faker

fake = Faker()
class SearchCustomerRegisterControllerSpy:
    def __init__(self) -> None:
        self.data = {} 

    def process(self, data: Dict, db_name: str) -> any:
        self.data = data
        if self.data:
            return fake.name()
        return None  


def test_search():
    search_customer_controller = SearchCustomerRegisterControllerSpy()
    payload = {
        "nome": fake.name(),
    }

    result = search_customer_controller.process(payload, fake.name())

    # Testing input
    assert search_customer_controller.data == payload

    # Testing output
    assert result is not None
