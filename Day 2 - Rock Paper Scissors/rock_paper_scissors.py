class RockPaperScissors:
    def __init__(self, strategy_guide: str):
        self.strategy_guide = strategy_guide

    def outcome(self) -> str:
        if self.strategy_guide.startswith("A"):
            return "win"
        if self.strategy_guide.startswith("B"):
            return "loss"
        return "draw"
