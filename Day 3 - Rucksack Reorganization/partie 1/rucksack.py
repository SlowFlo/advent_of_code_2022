class Rucksack:

    def __init__(self, items: str):
        self.first_compartment = items[:len(items)//2]
        self.second_compartment = items[len(items)//2:]

    @property
    def first_compartment(self) -> str:
        return self._first_compartment

    @first_compartment.setter
    def first_compartment(self, value: str):
        self._first_compartment = value

    @property
    def second_compartment(self) -> str:
        return self._second_compartment

    @second_compartment.setter
    def second_compartment(self, value: str):
        self._second_compartment = value
