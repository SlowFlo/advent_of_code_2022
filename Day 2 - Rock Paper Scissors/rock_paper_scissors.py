from aenum import MultiValueEnum


class Shape(MultiValueEnum):
    ROCK = "A", "X"
    PAPER = "B", "Y"
    SCISSORS = "C", "Z"


class RockPaperScissors:
    def __init__(self, strategy_guide: str):
        self.strategy_guide = strategy_guide

    @staticmethod
    def _has_my_shape_win(my_shape: Shape, opponent_shape: Shape) -> bool:
        if my_shape == Shape.ROCK and opponent_shape == Shape.SCISSORS:
            return True
        if my_shape == Shape.SCISSORS and opponent_shape == Shape.PAPER:
            return True
        if my_shape == Shape.PAPER and opponent_shape == Shape.ROCK:
            return True
        return False

    def outcome(self) -> str:
        shapes = self.strategy_guide.split()
        opponent_shape = Shape(shapes[0])
        my_shape = Shape(shapes[1])

        if opponent_shape == my_shape:
            return "draw"

        if self._has_my_shape_win(my_shape, opponent_shape):
            return "win"

        return "loss"
