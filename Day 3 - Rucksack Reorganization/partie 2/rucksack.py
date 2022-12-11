import re


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

    @staticmethod
    def calculate_pririty(item: str) -> int:
        if ord("a") <= ord(item) <= ord("z"):
            return ord(item) - ord("a") + 1
        return ord(item) - ord("A") + 27

    def get_priority(self) -> int:
        duplicate = self.find_duplicate()
        return self.calculate_pririty(duplicate)


class RucksackManager:
    def __init__(self, rucksacks_items: str):
        self.rucksacks_items = rucksacks_items
        rucksacks_list = rucksacks_items.splitlines()
        self.rucksacks = map(Rucksack, rucksacks_list)

    def get_total_priority(self) -> int:
        return sum(map(Rucksack.get_priority, self.rucksacks))

    def get_groups(self) -> list[str]:
        groups = re.findall(r"(?:^.+$\n?){1,3}", self.rucksacks_items, re.MULTILINE)
        return list(map(str.rstrip, groups))

    @staticmethod
    def _get_group_badge(group) -> str:
        groups_sets = list(map(set, group.splitlines()))
        return groups_sets[0].intersection(groups_sets[1]).intersection(groups_sets[2]).pop()

    def get_groups_badges(self) -> list[str]:
        groups = self.get_groups()

        return list(map(self._get_group_badge, groups))

    def get_badges_priority(self) -> int:
        badges = self.get_groups_badges()

        return sum(map(Rucksack.calculate_pririty, badges))


if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        input_text = file.read()
        my_rucksack_manager = RucksackManager(input_text)
        print(f"The total priority is {my_rucksack_manager.get_total_priority()}.")
