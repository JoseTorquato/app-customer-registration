from src.controller.customer_register_controller import \
    CustomerRegisterController
from src.models.repository import Repository


def customer_registration_composer():
    repository = Repository()
    customer_register_controller = CustomerRegisterController(repository)
