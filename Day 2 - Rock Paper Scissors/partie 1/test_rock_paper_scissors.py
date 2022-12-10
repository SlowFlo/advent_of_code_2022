from rock_paper_scissors import RockPaperScissors, Shape


def test_outcome_win_is_correct():
    assert RockPaperScissors.outcome(Shape("A"), Shape("Y")) == "win"
    assert RockPaperScissors.outcome(Shape("B"), Shape("Z")) == "win"


def test_outcome_loss_is_correct():
    assert RockPaperScissors.outcome(Shape("B"), Shape("X")) == "loss"


def test_outcome_draw_is_correct():
    assert RockPaperScissors.outcome(Shape("C"), Shape("Z")) == "draw"


def test_has_my_shape_win():
    assert not RockPaperScissors._has_my_shape_win(Shape.ROCK, Shape.ROCK)
    assert not RockPaperScissors._has_my_shape_win(Shape.ROCK, Shape.PAPER)
    assert RockPaperScissors._has_my_shape_win(Shape.ROCK, Shape.SCISSORS)

    assert RockPaperScissors._has_my_shape_win(Shape.PAPER, Shape.ROCK)
    assert not RockPaperScissors._has_my_shape_win(Shape.PAPER, Shape.PAPER)
    assert not RockPaperScissors._has_my_shape_win(Shape.PAPER, Shape.SCISSORS)

    assert not RockPaperScissors._has_my_shape_win(Shape.SCISSORS, Shape.ROCK)
    assert RockPaperScissors._has_my_shape_win(Shape.SCISSORS, Shape.PAPER)
    assert not RockPaperScissors._has_my_shape_win(Shape.SCISSORS, Shape.SCISSORS)


def test_calculate_simple_score():
    assert RockPaperScissors._score_by_round("A Y") == 8
    assert RockPaperScissors._score_by_round("B X") == 1
    assert RockPaperScissors._score_by_round("C Z") == 6


def test_calculate_complex_score():
    strategy_guide = """A Y
    B X
    C Z"""

    my_game = RockPaperScissors(strategy_guide)
    assert my_game.total_score() == 15
