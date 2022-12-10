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

    @classmethod
    def _score_by_round(cls, shapes: str) -> int:
        shapes_list = shapes.split()
        opponent_shape = Shape(shapes_list[0])
        my_shape = Shape(shapes_list[1])

        score = 0
        if my_shape == Shape.ROCK:
            score += 1
        elif my_shape == Shape.PAPER:
            score += 2
        elif my_shape == Shape.SCISSORS:
            score += 3

        round_outcome = cls.outcome(opponent_shape, my_shape)

        if round_outcome == "draw":
            score += 3
        elif round_outcome == "win":
            score += 6

        return score

    @classmethod
    def outcome(cls, opponent_shape: Shape, my_shape: Shape) -> str:
        if opponent_shape == my_shape:
            return "draw"

        return "win" if cls._has_my_shape_win(my_shape, opponent_shape) else "loss"

    def total_score(self) -> int:
        strategy_guide_lines = self.strategy_guide.splitlines()

        return sum(map(self._score_by_round, strategy_guide_lines))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_text = file.read()
        my_game = RockPaperScissors(input_text)
        print("The total score is", my_game.total_score(), "points.")