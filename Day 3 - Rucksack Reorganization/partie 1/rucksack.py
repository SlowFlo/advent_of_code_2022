class Rucksack:
    def __init__(self, items: str):
        self.first_compartment = items[: len(items) // 2]
        self.second_compartment = items[len(items) // 2 :]

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

    def find_duplicate(self) -> str:
        return set(self.first_compartment).intersection(self.second_compartment).pop()

    def get_priority(self) -> int:
        duplicate = self.find_duplicate()
        if ord("a") <= ord(duplicate) <= ord("z"):
            return ord(duplicate) - ord("a") + 1
        return ord(duplicate) - ord("A") + 27
