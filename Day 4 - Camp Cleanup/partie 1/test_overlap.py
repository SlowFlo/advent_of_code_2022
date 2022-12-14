from overlap import Binome


def test_get_each_section():
    binome1 = Binome("2-4,6-8")
    assert binome1.first_elf == [2, 3, 4]
    assert binome1.second_elf == [6, 7, 8]

    binome2 = Binome("2-8,3-7")
    assert binome2.first_elf == [2, 3, 4, 5, 6, 7, 8]
    assert binome2.second_elf == [3, 4, 5, 6, 7]

    binome3 = Binome("2-6,4-8")
    assert binome3.first_elf == [2, 3, 4, 5, 6]
    assert binome3.second_elf == [4, 5, 6, 7, 8]

    binome4 = Binome("84-88,93-93")
    assert binome4.first_elf == [84, 85, 86, 87, 88]
    assert binome4.second_elf == [93]

