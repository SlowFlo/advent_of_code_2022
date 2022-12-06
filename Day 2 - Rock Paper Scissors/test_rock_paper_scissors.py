from rock_paper_scissors import RockPaperScissors


def test_predict_win_correctly():
    assert RockPaperScissors.is_a_win("A", "Y")


def test_predict_loose_correctly():
    assert not RockPaperScissors.is_a_win("B", "X")
