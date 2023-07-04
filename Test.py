#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.rolls(pins)

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.rolls(0)
        self.assertEqual(self.game.score(), 0, "Should be 0")

    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20, "Should be 20")

    def testOneSpare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        self.assertEqual(self.game.score(), 16, "Should be 16")

    def testOneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        self.assertEqual(self.game.score(), 24, "Should be 24")

    def testPerfectGame(self):
        self.rollMany(10,12)
        self.assertEqual(self.game.score(), 300, "Should be 300")

    def testOneSpare(self):
        self.rollMany(5,21)
        self.assertEqual(self.game.score(), 150, "Should be 150")

if __name__ == '__main__':
    unittest.main()