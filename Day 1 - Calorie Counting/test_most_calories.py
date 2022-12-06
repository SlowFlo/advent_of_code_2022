from most_calories import most_calories, sum_calories, sum_first_three_inventories


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


def test_get_the_sum_of_the_first_three_inventories():
    input_str = """
        1000
        2000
        3000

        4000
        
        5000
        6000
        
        7000
        8000
        9000
        
        10000
        """
    assert sum_first_three_inventories(input_str) == 45000
