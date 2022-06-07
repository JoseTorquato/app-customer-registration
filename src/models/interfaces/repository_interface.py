from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def migrate(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def select(self):
        pass
