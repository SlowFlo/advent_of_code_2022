from enum import Enum


class Shape(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class Goal(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


class RockPaperScissors:
    def __init__(self, strategy_guide: str):
        self.strategy_guide = strategy_guide

    @classmethod
    def _score_by_round(cls, strategy_guide_line: str) -> int:
        instruction_list = strategy_guide_line.split()
        opponent_shape = Shape(instruction_list[0])
        my_goal = Goal(instruction_list[1])

        my_shape = cls._find_goal(opponent_shape, my_goal)

        score = 0
        if my_shape == Shape.ROCK:
            score += 1
        elif my_shape == Shape.PAPER:
            score += 2
        elif my_shape == Shape.SCISSORS:
            score += 3

        if my_goal == Goal.DRAW:
            score += 3
        elif my_goal == Goal.WIN:
            score += 6

        return score

    @classmethod
    def _find_goal(cls, opponent_shape: Shape, my_goal: Goal) -> Shape:
        if my_goal is Goal.DRAW:
            return opponent_shape
        if my_goal is Goal.WIN:
            if opponent_shape is Shape.ROCK:
                return Shape.PAPER
            if opponent_shape is Shape.PAPER:
                return Shape.SCISSORS
            if opponent_shape is Shape.SCISSORS:
                return Shape.ROCK
        else:
            if opponent_shape is Shape.ROCK:
                return Shape.SCISSORS
            if opponent_shape is Shape.PAPER:
                return Shape.ROCK
            if opponent_shape is Shape.SCISSORS:
                return Shape.PAPER

    def total_score(self) -> int:
        strategy_guide_lines = self.strategy_guide.splitlines()

        return sum(map(self._score_by_round, strategy_guide_lines))


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_text = file.read()
        my_game = RockPaperScissors(input_text)
        print("The total score is", my_game.total_score(), "points.")
