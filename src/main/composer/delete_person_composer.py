from src.controller.delete_person_controller import \
    DeleteCustomerRegisterController
from src.models.repository import Repository
from src.views.customer_register_view import CustomerRegisterView


def delete_customer_registration_composer():
    repository = Repository()
    customer_register_controller = DeleteCustomerRegisterController(repository)
    customer_register_view = CustomerRegisterView(customer_register_controller)
    return customer_register_view
