from abc import ABC, abstractmethod


class CustomerRegisterInterface(ABC):

    @abstractmethod
    def create_person(self):
        pass
    
    @abstractmethod
    def get_person(self):
        pass
