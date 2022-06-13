from src.controller.update_person_controller import \
    UpdateCustomerRegisterController
from src.models.repository import Repository
from src.views.customer_register_view import CustomerRegisterView


def update_customer_registration_composer():
    repository = Repository()
    customer_register_controller = UpdateCustomerRegisterController(repository)
    customer_register_view = CustomerRegisterView(customer_register_controller)
    return customer_register_view
