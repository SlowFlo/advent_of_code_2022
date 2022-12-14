class Binome:
    def __init__(self, binome: str):
        self.generate_sections(binome)

    def generate_sections(self, binome: str):
        elves_sections = binome.split(",")

        first_elf_range = elves_sections[0].split("-")
        second_elf_range = elves_sections[1].split("-")

        self.first_elf = list(range(int(first_elf_range[0]), int(first_elf_range[1]) + 1))
        self.second_elf = list(range(int(second_elf_range[0]), int(second_elf_range[1]) + 1))

