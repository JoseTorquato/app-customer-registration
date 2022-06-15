from faker import Faker

fake = Faker()
class CustomerRegisterControllerSpy:
    def __init__(self) -> None:
        self.data = ""

    def process(self,  db_name: str) -> any:
        self.data = db_name

        if db_name:
            return fake.name()
        return None  


def test_search():
    customer_controller = CustomerRegisterControllerSpy()

    db = fake.name()
    result = customer_controller.process(db)

    # Testing input
    assert customer_controller.data == db

    # Testing output
    assert result is not None
