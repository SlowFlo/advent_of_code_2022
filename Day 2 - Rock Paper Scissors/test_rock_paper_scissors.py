from rock_paper_scissors import RockPaperScissors, Shape


def test_outcome_win_is_correct():
    my_game = RockPaperScissors("A Y")
    assert my_game.outcome() == "win"

    my_game = RockPaperScissors("B Z")
    assert my_game.outcome() == "win"


def test_outcome_loss_is_correct():
    my_game = RockPaperScissors("B X")
    assert my_game.outcome() == "loss"


def test_outcome_draw_is_correct():
    my_game = RockPaperScissors("C Z")
    assert my_game.outcome() == "draw"


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
