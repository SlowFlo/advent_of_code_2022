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


class RucksackManager:
    def __init__(self, rucksacks_items: str):
        rucksacks_list = rucksacks_items.splitlines()
        self.rucksacks = map(Rucksack, rucksacks_list)

    def get_total_priority(self) -> int:
        return sum(map(Rucksack.get_priority, self.rucksacks))


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        my_rucksack_manager = RucksackManager(input_text)
        print(f"The total priority is {my_rucksack_manager.get_total_priority()}.")
