class Rucksack:

    def __init__(self, items: str):
        self.first_compartement = items[:len(items)//2]
        self.second_compartement = items[len(items)//2:]