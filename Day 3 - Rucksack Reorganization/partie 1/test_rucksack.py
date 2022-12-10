from rucksack import Rucksack


def test_get_compartments_content():
    my_rucksack = Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert my_rucksack.first_compartement == "vJrwpWtwJgWr"
    assert my_rucksack.second_compartement == "hcsFMMfFFhFp"
