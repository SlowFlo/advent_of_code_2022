from overlap import get_sections


def test_get_each_section():
    assert get_sections("2-4,6-8") == {"first_elf": [2, 3, 4], "second_elf": [6, 7, 8]}
    assert get_sections("2-8,3-7") == {"first_elf": [2, 3, 4, 5, 6, 7, 8], "second_elf": [3, 4, 5, 6, 7]}
    assert get_sections("2-6,4-8") == {"first_elf": [2, 3, 4, 5, 6], "second_elf": [4, 5, 6, 7, 8]}
    assert get_sections("84-88,93-93") == {"first_elf": [84, 85, 86, 87, 88], "second_elf": [93]}
