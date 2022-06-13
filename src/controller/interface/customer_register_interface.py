from abc import ABC, abstractmethod


class CustomerRegisterInterface(ABC):

    @abstractmethod
    def process(self):
        pass
