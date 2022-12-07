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

        return my_shape == Shape.PAPER and opponent_shape == Shape.ROCK

    def outcome(self) -> str:
        shapes = self.strategy_guide.split()
        opponent_shape = Shape(shapes[0])
        my_shape = Shape(shapes[1])

        if opponent_shape == my_shape:
            return "draw"

        return "win" if self._has_my_shape_win(my_shape, opponent_shape) else "loss"

    def score(self) -> int:
        shapes = self.strategy_guide.split()
        my_shape = Shape(shapes[1])

        score = 0
        if my_shape == Shape.ROCK:
            score += 1
        elif my_shape == Shape.PAPER:
            score += 2
        elif my_shape == Shape.SCISSORS:
            score += 3

        if self.outcome() == "draw":
            score += 3
        elif self.outcome() == "win":
            score += 6

        return score
