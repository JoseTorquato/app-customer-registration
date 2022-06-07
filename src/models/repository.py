from src.database.manager_db import manager_db
from src.models.interfaces.repository_interface import RepositoryInterface


class Repository(RepositoryInterface):
    def migrate(self):
        manager_db.migrate()

    def create(self):
        manager_db.insert_person()

    def update(self):
        manager_db.update_person()

    def delete(self):
        manager_db.delete_person()

    def select(self):
        return manager_db.get_all_persons()
