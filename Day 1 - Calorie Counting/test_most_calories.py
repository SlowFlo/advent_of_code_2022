from most_calories import most_calories, sum_calories


def test_empty_str_is_0():
    input_str = ""
    assert sum_calories(input_str) == 0


def test_simple_str_is_converted_to_int():
    input_str = "100"
    assert sum_calories(input_str) == 100


def test_multiline_str_is_additionned():
    input_str = """100
        200"""
    assert sum_calories(input_str) == 300


def test_empty_or_blank_lines_are_ok():
    input_str = """
        100
        200
        """
    assert sum_calories(input_str) == 300


def test_several_inventories_return_the_max():
    input_str = """
        100
        200
        
        300
        400
        """
    assert most_calories(input_str) == 700
