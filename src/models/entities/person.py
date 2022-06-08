from typing import Dict, Tuple


class Person:
    def __init__(self, data: Dict) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.age = data["age"]
        self.district = data["district"]
        self.profession = data["profession"]

    def get_values(self) -> Tuple:
        return (self.name, self.age, self.district, self.profession, self.id)
