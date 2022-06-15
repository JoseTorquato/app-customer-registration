import sqlite3

import pytest
from src.controller.create_person_controller import \
    CreateCustomerRegisterController
from src.controller.customer_register_controller import \
    CustomerRegisterController
from src.controller.delete_person_controller import \
    DeleteCustomerRegisterController
from src.controller.search_person_controller import \
    SearchCustomerRegisterController
from src.controller.update_person_controller import \
    UpdateCustomerRegisterController
from src.models.repository import Repository

repository = Repository()
controller = CustomerRegisterController(repository)
person_controller = CustomerRegisterController(repository)
create_person_controller = CreateCustomerRegisterController(repository)
update_person_controller = UpdateCustomerRegisterController(repository)
delete_person_controller = DeleteCustomerRegisterController(repository)
search_person_controller = SearchCustomerRegisterController(repository)

def test_search_person_by_name_not_exist():
    repository.migrate("customer_registration_test.db")

    assert search_person_controller.process({"name": "José"}, "customer_registration_test.db") == {"message": "Não existe cliente com esse nome", "success": False}
    assert search_person_controller.process({"name": "Pedro"}, "customer_registration_test.db")["message"] == "Não existe cliente com esse nome"
    assert search_person_controller.process({"name": "Maria"}, "customer_registration_test.db")["success"] == False

def test_create_person():
    assert create_person_controller.process({"name": "José", "age": 25, "district": "", "profession": ""}, "customer_registration_test.db") == {'message': 'Cliente José criado com sucesso.', 'success':True}
    assert create_person_controller.process({"name": "Pedro", "age": 26, "district": "Guajuviras", "profession": ""}, "customer_registration_test.db")["message"] == 'Cliente Pedro criado com sucesso.'
    assert create_person_controller.process({"name": "Maria", "age": 45, "district": "Estância", "profession": "Developer"}, "customer_registration_test.db")["success"] == True

def test_search_person_by_name_exist():
    assert search_person_controller.process({"name": "José"}, "customer_registration_test.db") == {'age': 25, 'district': None, 'id': 1, 'name': 'José', 'profession': None}
    assert search_person_controller.process({"name": "Pedro"}, "customer_registration_test.db") == {"age": 26, "name": "Pedro", "district": "Guajuviras", "id": 2, "profession": None}
    assert search_person_controller.process({"name": "Maria"}, "customer_registration_test.db") == {"age": 45, "name": "Maria", "district": "Estância", "id":3, "profession": "Developer"}

def test_update_person():
    assert update_person_controller.process({"name": "José", "age": 34, "district": "Teste Update", "profession": ""}, "customer_registration_test.db") == {'message': 'Dados do cliente José alterado com sucesso.', 'success':True}
    assert update_person_controller.process({"name": "Pedro", "district": "Guajuviras", "profession": "Teste Update"}, "customer_registration_test.db")["message"] == 'Dados do cliente Pedro alterado com sucesso.'
    assert update_person_controller.process({"name": "Maria", "age": 45, "district": "Teste"}, "customer_registration_test.db")["success"] == True

def test_search_person_by_name_exist_update():
    assert search_person_controller.process({"name": "José"}, "customer_registration_test.db") == {'age': 34, 'district': 'Teste Update', 'id': 1, 'name': 'José', 'profession': None}
    assert search_person_controller.process({"name": "Pedro"}, "customer_registration_test.db") == {"age": None, "name": "Pedro", "district": "Guajuviras", "id": 2, "profession": "Teste Update"}
    assert search_person_controller.process({"name": "Maria"}, "customer_registration_test.db") == {"age": 45, "name": "Maria", "district": "Teste", "id":3, "profession": None}

def test_delete_person():
    assert delete_person_controller.process({"name": "Pedro"}, "customer_registration_test.db")["message"] == 'Cliente Pedro deletado com sucesso.'
    assert delete_person_controller.process({"name": "Maria"}, "customer_registration_test.db")["success"] == True
    assert delete_person_controller.process({"name": "José"}, "customer_registration_test.db") == {'message': 'Cliente José deletado com sucesso.', 'success':True}

def test_search_person_by_name_not_exist_delete():
    assert search_person_controller.process({"name": "José"}, "customer_registration_test.db") == {"message": "Não existe cliente com esse nome", "success": False}
    assert search_person_controller.process({"name": "Pedro"}, "customer_registration_test.db")["message"] == "Não existe cliente com esse nome"
    assert search_person_controller.process({"name": "Maria"}, "customer_registration_test.db")["success"] == False
    
    drop_table_test()

def drop_table_test():
    conn = sqlite3.connect("customer_registration_test.db")
    cursor = conn.cursor()
    cursor.execute("DROP table persons;")
    conn.commit()
    conn.close()
