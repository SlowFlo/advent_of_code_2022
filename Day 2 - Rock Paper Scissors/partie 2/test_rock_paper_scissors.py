from rock_paper_scissors import RockPaperScissors, Shape, Goal


def test_goal_is_correct():
    assert RockPaperScissors._find_goal(Shape("A"), Goal("Y")) == Shape.ROCK
    assert RockPaperScissors._find_goal(Shape("B"), Goal("X")) == Shape.ROCK
    assert RockPaperScissors._find_goal(Shape("C"), Goal("Z")) == Shape.ROCK


def test_calculate_simple_score():
    assert RockPaperScissors._score_by_round("A Y") == 4
    assert RockPaperScissors._score_by_round("B X") == 1
    assert RockPaperScissors._score_by_round("C Z") == 7


def test_calculate_complex_score():
    strategy_guide = """A Y
    B X
    C Z"""

    my_game = RockPaperScissors(strategy_guide)
    assert my_game.total_score() == 12
