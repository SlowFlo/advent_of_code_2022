from rucksack import Rucksack


def test_get_compartments_content():
    my_rucksack = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert my_rucksack.first_compartment == "vJrwpWtwJgWr"
    assert my_rucksack.second_compartment == "hcsFMMfFFhFp"
