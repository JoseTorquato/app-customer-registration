
from src.controller.search_person_controller import \
    SearchCustomerRegisterController
from src.models.repository import Repository
from src.views.customer_register_view import CustomerRegisterView


def search_customer_registration_composer():
    repository = Repository()
    customer_register_controller = SearchCustomerRegisterController(repository)
    customer_register_view = CustomerRegisterView(customer_register_controller)
    return customer_register_view
