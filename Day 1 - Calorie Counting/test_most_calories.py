from most_calories import most_calories


def test_empty_str_is_0():
    input_str = ""
    assert most_calories(input_str) == 0


def test_simple_str_is_converted_to_int():
    input_str = "100"
    assert most_calories(input_str) == 100
