#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def rollMany(self, pins, rolls):
        """
        Appends a specified amount of pins scored in a roll 
        to the list of rolls a specified amount of times.

        args:
        self: this 
        pins(int): How many pins have been hit in this roll
        rolls(int): How many rolls should be added to the list with this amount of pins

        Returns: 
        None
        """
        for i in range(rolls):
            self.game.roll(pins)

    def testGutterGame(self):
        '''
        Tests a gutter game - a game where every ball gutters and no points are scored.

        args: 
        arg 1: Bowling Game  

        Returns: bool True if equal, otherwise False
        '''
        self.rollMany(0, 20)
        self.assertEqual(self.game.score(), 0, "Should be 0")

    def testAllOnes(self):
        '''
        Test score if every roll is a one

        args: 
        arg 1: self

        Returns: bool True if equal, otherwise False
        '''
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20, "Should be 20")

    def testOneSpare(self):
        '''
        Test score if there is one spare rolled in the game, and
        no other points are scored except for the spare and the doubled point roll. 

        args:
        arg 1: self

        Returns: bool True if equal, otherwise False
        '''
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        self.assertEqual(self.game.score(), 16, "Should be 16")

    def testOneStrike(self):
        '''
        Test score if there is one strike rolled in the game, and no other
        points are scored except the strike and the two double point rolls. 

        args: 
        arg 1: self

        Returns: bool True if equal, otherwise False
        '''
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        self.assertEqual(self.game.score(), 24, "Should be 24")

    def testPerfectGame(self):
        '''
        Test result if player runs a perfect game of all strikes

        args:
        arg 1: self

        Returns: bool True if equal, otherwise False
        '''
        self.rollMany(10,12)
        self.assertEqual(self.game.score(), 300, "Should be 300")

    def testAllSpare(self):
        '''
        Test score if player rolls a game of all spares.

        args:
        arg 1: self

        Returns: bool True if equal, otherwise False
        '''
        self.rollMany(5,21)
        self.assertEqual(self.game.score(), 150, "Should be 150")

    def testStrikeInLastFrame(self):
        """
        Test Score if player rolls a strike in the last frame
        
        args:
        arg 1: sself
        
        Returns: bool True if equal, otherwise False
        """
        self.rollMany(0, 18)
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(10)
        self.assertEqual(self.game.score(), 30, 'Should equal 30')

    def testSpareInLastFrame(self):
        """
        Test Score if player rolls a strike in the last frame
        
        args:
        arg 1: sself
        
        Returns: bool True if equal, otherwise False
        """
        self.rollMany(0, 18)
        self.game.roll(5)
        self.game.roll(5)
        self.assertEqual(self.game.score(), 10, 'Should equal 10')

if __name__ == '__main__':
    unittest.main()