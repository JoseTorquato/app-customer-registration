from src.errors.validators_errors import SystemErrors
from src.models.database.manager_db import manager_db
from src.models.entities.person import Person
from src.models.interfaces.repository_interface import RepositoryInterface


class Repository(RepositoryInterface):
    def migrate(self, db_name="customer_registration.db"):
        return manager_db.migrate(db_name)

    def create(self, data, db_name="customer_registration.db"):
        try:
            if not data.get("age", ""):
                data["age"] = None 

            if not data.get("profession", ""):
                data["profession"] = None

            if not data.get("district", ""):
                data["district"] = None
                
            person = Person(data)
            return manager_db.insert_person(person, db_name)
        except Exception as exception:
            raise SystemErrors(str(exception))

    def update(self, data, db_name="customer_registration.db"):
        try:
            search = self.search_by_name(data["name"], db_name)
            search["age"] = None
            search["profession"] = None
            search["district"] = None

            if data.get("age", ""):
                search["age"] = data["age"] 

            if data.get("profession", ""):
                search["profession"] = data["profession"]

            if data.get("district", ""):
                search["district"] = data["district"]
            
            person = Person(search)
            return manager_db.update_person(person, db_name)
        except Exception as exception:
            raise RepositoryErrors(str(exception))

    def delete(self, data, db_name="customer_registration.db"):
        search = self.search_by_name(data["name"], db_name)
        person = Person(search)
        return manager_db.delete_person(person, db_name)

    def search_by_name(self, name, db_name="customer_registration.db"):
        return manager_db.get_person_by_name(name,db_name)

    def select(self, db_name="customer_registration.db"):
        return manager_db.get_all_persons(db_name)
