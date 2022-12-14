def get_sections(binome: str) -> dict[str, list[int]]:
    elves_sections = binome.split(",")

    sections = {}

    first_elf_range = elves_sections[0].split("-")
    second_elf_range = elves_sections[1].split("-")

    sections["first_elf"] = list(range(int(first_elf_range[0]), int(first_elf_range[1]) + 1))
    sections["second_elf"] = list(range(int(second_elf_range[0]), int(second_elf_range[1]) + 1))

    return sections
