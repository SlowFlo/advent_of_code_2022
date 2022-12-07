from rock_paper_scissors import RockPaperScissors


def test_predict_win_correctly():
    my_game = RockPaperScissors("A Y")
    assert my_game.is_a_win()


def test_predict_loose_correctly():
    my_game = RockPaperScissors("B X")
    assert not my_game.is_a_win()
