from rucksack import Rucksack, RucksackManager


def test_get_compartments_content():
    my_rucksack = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert my_rucksack.first_compartment == "vJrwpWtwJgWr"
    assert my_rucksack.second_compartment == "hcsFMMfFFhFp"

    my_rucksack = Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    assert my_rucksack.first_compartment == "jqHRNqRjqzjGDLGL"
    assert my_rucksack.second_compartment == "rsFMfFZSrLrFZsSL"

    my_rucksack = Rucksack("PmmdzqPrVvPwwTWBwg")
    assert my_rucksack.first_compartment == "PmmdzqPrV"
    assert my_rucksack.second_compartment == "vPwwTWBwg"


def test_find_duplicate():
    my_rucksack = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert my_rucksack.find_duplicate() == "p"

    my_rucksack = Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    assert my_rucksack.find_duplicate() == "L"

    my_rucksack = Rucksack("PmmdzqPrVvPwwTWBwg")
    assert my_rucksack.find_duplicate() == "P"

    my_rucksack = Rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    assert my_rucksack.find_duplicate() == "v"

    my_rucksack = Rucksack("ttgJtRGJQctTZtZT")
    assert my_rucksack.find_duplicate() == "t"

    my_rucksack = Rucksack("CrZsJsPPZsGzwwsLwLmpwMDw")
    assert my_rucksack.find_duplicate() == "s"


def test_get_priority():
    my_rucksack = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert my_rucksack.get_priority() == 16

    my_rucksack = Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    assert my_rucksack.get_priority() == 38

    my_rucksack = Rucksack("PmmdzqPrVvPwwTWBwg")
    assert my_rucksack.get_priority() == 42

    my_rucksack = Rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
    assert my_rucksack.get_priority() == 22

    my_rucksack = Rucksack("ttgJtRGJQctTZtZT")
    assert my_rucksack.get_priority() == 20

    my_rucksack = Rucksack("CrZsJsPPZsGzwwsLwLmpwMDw")
    assert my_rucksack.get_priority() == 19


def test_get_total_priority():
    my_rucksack_manager = RucksackManager(
        """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    )

    assert my_rucksack_manager.get_total_priority() == 157


def test_get_groups():
    my_rucksack_manager = RucksackManager(
        """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    )

    assert my_rucksack_manager.get_groups() == [
        """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg""",
        """wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""",
    ]


def test_find_groups_badges():
    my_rucksack_manager = RucksackManager(
        """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    )

    assert my_rucksack_manager.get_groups_badges() == ["r", "Z"]


def test_find_badge_of_one_group():
    group = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg"""

    assert RucksackManager._get_group_badge(group) == "r"
