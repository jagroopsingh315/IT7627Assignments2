import unittest
from bowling_game import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """
    Comprehensive test suite for the BowlingGame class.
    This suite aligns with the provided test plan to ensure excellent coverage
    of all bowling rules, scoring scenarios, and edge cases.
    """

    def setUp(self):
        """Initialize a new BowlingGame before every test."""
        self.game = BowlingGame()

    def roll_many(self, pins, rolls):
        """Helper method to roll the same number of pins multiple times."""
        for _ in range(rolls):
            self.game.roll(pins)

    def roll_array(self, rolls_array):
        """Helper method to process a specific sequence of rolls."""
        for pins in rolls_array:
            self.game.roll(pins)

    # TC-01: Gutter Game
    def test_gutter_game(self):
        """Test a game where no pins are knocked down (20 rolls of 0)."""
        self.roll_many(0, 20)
        self.assertEqual(0, self.game.score(), "Gutter game should score 0")

    # TC-02: All Ones
    def test_all_ones(self):
        """Test basic open frame addition with no bonuses (20 rolls of 1)."""
        self.roll_many(1, 20)
        self.assertEqual(20, self.game.score(), "All ones should score 20")

    # TC-03: Regular Game
    def test_regular_game(self):
        """Test a standard game containing no strikes or spares."""
        rolls = [3, 4, 2, 5, 1, 6, 4, 2, 8, 1, 7, 1, 5, 3, 2, 3, 4, 3, 2, 6]
        self.roll_array(rolls)
        self.assertEqual(72, self.game.score(), "Regular game should score 72")

    # TC-04: Single Spare
    def test_single_spare(self):
        """Test the spare bonus logic (10 pins + first ball of the next frame)."""
        self.roll_array([4, 6, 5, 2]) # Spare in frame 1, open in frame 2
        self.roll_many(0, 16)         # Miss the rest of the game
        self.assertEqual(22, self.game.score(), "Single spare should correctly add bonus")

    # TC-05: Single Strike
    def test_single_strike(self):
        """Test the strike bonus logic (10 pins + next two balls)."""
        self.roll_array([10, 3, 6])   # Strike in frame 1, open in frame 2
        self.roll_many(0, 16)         # Miss the rest of the game
        self.assertEqual(28, self.game.score(), "Single strike should correctly add bonus")

    # TC-06: Consecutive Strikes
    def test_consecutive_strikes(self):
        """Test cascading strike bonuses and look-ahead logic."""
        self.roll_array([10, 10, 4, 2]) # Strikes in frame 1 & 2, open in frame 3
        self.roll_many(0, 14)           # Miss the rest of the game
        self.assertEqual(46, self.game.score(), "Consecutive strikes should cascade bonuses correctly")

    # TC-07: All Spares Game
    def test_all_spares(self):
        """Test spare logic applied to every frame, specifically the 3rd bonus ball in the 10th frame."""
        self.roll_many(5, 21) # 10 frames of 2 rolls each, plus 1 bonus roll
        self.assertEqual(150, self.game.score(), "All spares should correctly handle 10th frame bonus ball")

    # TC-08: Perfect Game
    def test_perfect_game(self):
        """Test the maximum score, consecutive strikes, and the 10th frame 3-strike rule."""
        self.roll_many(10, 12) # 10 frames of 1 roll each, plus 2 bonus rolls
        self.assertEqual(300, self.game.score(), "Perfect game should score 300")

    # TC-09: Client Example Game
    def test_client_example_game(self):
        """Test the exact scenario provided in the project brief."""
        rolls = [10, 3, 6, 5, 5, 8, 1, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]
        self.roll_array(rolls)
        self.assertEqual(190, self.game.score(), "Client example game should score 190")

if __name__ == '__main__':
    unittest.main()
