"""
Bowling Game Implementation
A module for calculating standard 10-pin bowling game scores.
"""

class BowlingGame:
    """
    Calculates the score of a 10-pin bowling game based on a series of rolls.
    Handles standard scoring rules including strikes, spares, and open frames,
    as well as 10th-frame bonus rolls.
    """
    
    # Constants to eliminate magic numbers and improve readability
    MAX_PINS = 10
    TOTAL_FRAMES = 10

    def __init__(self):
        """Initializes a new game with an empty list of rolls."""
        self.rolls = []

    def roll(self, pins):
        """
        Records a roll in the game.
        
        Args:
            pins (int): The number of pins knocked down in this roll.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates the total score for the game.
        
        Returns:
            int: The final calculated score.
        """
        score = 0
        roll_index = 0

        for frame in range(self.TOTAL_FRAMES):
            if self._is_strike(roll_index):
                score += self.MAX_PINS + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                score += self.MAX_PINS + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2

        return score

    def _is_strike(self, roll_index):
        """Checks if the roll at the given index is a strike."""
        return roll_index < len(self.rolls) and self.rolls[roll_index] == self.MAX_PINS

    def _is_spare(self, roll_index):
        """Checks if the roll at the given index and the subsequent roll form a spare."""
        return roll_index + 1 < len(self.rolls) and self.rolls[roll_index] + self.rolls[roll_index + 1] == self.MAX_PINS

    def _strike_bonus(self, roll_index):
        """Calculates the bonus points for a strike."""
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def _spare_bonus(self, roll_index):
        """Calculates the bonus points for a spare."""
        return self.rolls[roll_index + 2]