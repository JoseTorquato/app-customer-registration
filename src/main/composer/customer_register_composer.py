from src.controller.customer_register_controller import \
    CustomerRegisterController
from src.models.repository import Repository
from src.views.customer_register_view import CustomerRegisterView


def customer_registration_composer():
    repository = Repository()
    print(repository)
    customer_register_controller = CustomerRegisterController(repository)
    print(customer_register_controller)
    customer_register_view = CustomerRegisterView(customer_register_controller)
    print(customer_register_view)
    return customer_register_view
