from src.controller.create_person_controller import \
    CreateCustomerRegisterController
from src.models.repository import Repository
from src.views.create_person_view import CreateCustomerRegisterView


def create_customer_registration_composer():
    repository = Repository()
    customer_register_controller = CreateCustomerRegisterController(repository)
    customer_register_view = CreateCustomerRegisterView(customer_register_controller)
    return customer_register_view
