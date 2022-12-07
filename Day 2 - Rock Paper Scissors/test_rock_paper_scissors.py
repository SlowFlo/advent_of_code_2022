from rock_paper_scissors import RockPaperScissors


def test_predict_win_correctly():
    my_game = RockPaperScissors("A Y")
    assert my_game.outcome() == "win"


def test_predict_loss_correctly():
    my_game = RockPaperScissors("B X")
    assert my_game.outcome() == "loss"


def test_predict_draw_correctly():
    my_game = RockPaperScissors("C Z")
    assert my_game.outcome() == "draw"
