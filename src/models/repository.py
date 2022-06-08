from src.database.manager_db import manager_db
from src.models.entities.person import Person
from src.models.interfaces.repository_interface import RepositoryInterface


class Repository(RepositoryInterface):
    def migrate(self):
        manager_db.migrate()

    def create(self, data):
        person = Person(data)
        return manager_db.insert_person(person)

    def update(self, data):
        search = self.search_by_name(data["name"])
        if data.get("age", ""):
            search["age"] = data["age"] 

        if data.get("profession", ""):
            search["profession"] = data["profession"]

        if data.get("district", ""):
            search["district"] = data["district"]
        
        person = Person(search)
        return manager_db.update_person(person)

    def delete(self, data):
        search = self.search_by_name(data["name"])
        person = Person(search)
        return manager_db.delete_person(person)

    def search_by_name(self, name):
        return manager_db.get_person_by_name(name)

    def select(self):
        return manager_db.get_all_persons()
