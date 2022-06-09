import sqlite3

import pytest
from src.controller.customer_register_controller import \
    CustomerRegisterController
from src.models.repository import Repository

repository = Repository()
controller = CustomerRegisterController(repository)

def test_search_person_by_name_not_exist():
    repository.migrate("customer_registration_test.db")

    assert controller.search_person({"name": "José"}, "customer_registration_test.db") == {"message": "Não existe cliente com esse nome", "success": False}
    assert controller.search_person({"name": "Pedro"}, "customer_registration_test.db")["message"] == "Não existe cliente com esse nome"
    assert controller.search_person({"name": "Maria"}, "customer_registration_test.db")["success"] == False

def test_create_person():
    assert controller.create_person({"name": "José", "age": 25, "district": "", "profession": ""}, "customer_registration_test.db") == {'message': 'Cliente José criado com sucesso.', 'success':True}
    assert controller.create_person({"name": "Pedro", "age": 26, "district": "Guajuviras", "profession": ""}, "customer_registration_test.db")["message"] == 'Cliente Pedro criado com sucesso.'
    assert controller.create_person({"name": "Maria", "age": 45, "district": "Estância", "profession": "Developer"}, "customer_registration_test.db")["success"] == True

def test_search_person_by_name_exist():
    assert controller.search_person({"name": "José"}, "customer_registration_test.db") == {'age': 25, 'district': '', 'id': 1, 'name': 'José', 'profession': ''}
    assert controller.search_person({"name": "Pedro"}, "customer_registration_test.db") == {"age": 26, "name": "Pedro", "district": "Guajuviras", "id": 2, "profession": ""}
    assert controller.search_person({"name": "Maria"}, "customer_registration_test.db") == {"age": 45, "name": "Maria", "district": "Estância", "id":3, "profession": "Developer"}

def test_update_person():
    assert controller.update_person({"name": "José", "age": 34, "district": "Teste Update", "profession": ""}, "customer_registration_test.db") == {'message': 'Dados do cliente José alterado com sucesso.', 'success':True}
    assert controller.update_person({"name": "Pedro", "district": "Guajuviras", "profession": "Teste Update"}, "customer_registration_test.db")["message"] == 'Dados do cliente Pedro alterado com sucesso.'
    assert controller.update_person({"name": "Maria", "age": 45, "district": "Teste"}, "customer_registration_test.db")["success"] == True

def test_search_person_by_name_exist_update():
    assert controller.search_person({"name": "José"}, "customer_registration_test.db") == {'age': 34, 'district': 'Teste Update', 'id': 1, 'name': 'José', 'profession': ''}
    assert controller.search_person({"name": "Pedro"}, "customer_registration_test.db") == {"age": 26, "name": "Pedro", "district": "Guajuviras", "id": 2, "profession": "Teste Update"}
    assert controller.search_person({"name": "Maria"}, "customer_registration_test.db") == {"age": 45, "name": "Maria", "district": "Teste", "id":3, "profession": "Developer"}

def test_delete_person():
    assert controller.delete_person({"name": "José"}, "customer_registration_test.db") == {'message': 'Cliente José deletado com sucesso.', 'success':True}
    assert controller.delete_person({"name": "Pedro"}, "customer_registration_test.db")["message"] == 'Cliente Pedro deletado com sucesso.'
    assert controller.delete_person({"name": "Maria"}, "customer_registration_test.db")["success"] == True

def test_search_person_by_name_not_exist_delete():
    assert controller.search_person({"name": "José"}, "customer_registration_test.db") == {"message": "Não existe cliente com esse nome", "success": False}
    assert controller.search_person({"name": "Pedro"}, "customer_registration_test.db")["message"] == "Não existe cliente com esse nome"
    assert controller.search_person({"name": "Maria"}, "customer_registration_test.db")["success"] == False
    
    drop_table_test()

def drop_table_test():
    conn = sqlite3.connect("customer_registration_test.db")
    cursor = conn.cursor()
    cursor.execute("DROP table persons;")
    conn.commit()
    conn.close()
