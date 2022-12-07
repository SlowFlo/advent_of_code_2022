class RockPaperScissors:
    def __init__(self, strategy_guide: str):
        self.strategy_guide = strategy_guide

    def is_a_win(self) -> bool:
        if self.strategy_guide.startswith("A"):
            return True
        return False
