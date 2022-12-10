from rucksack import Rucksack


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
