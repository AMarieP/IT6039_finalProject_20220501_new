#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        """
        Appends count of hit pins in a roll to array of rolls
        
        pins (int): How many pins have been hit in this roll
        
        Returns: None
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates total score from a game

        Returns: int
        """
        result = 0
        rollIndex = 0
        for frame in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        '''
        Calculates if frame was a Strike by checking if first roll is equal to 10

        rollIndex(int): the index number of the roll 

        Returns: bool True if it is a Strike, False if not
        '''
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        '''
        Calculates if frame was a Spare by checking if frame score is equal to 10

        rollIndex(int): the index number of the roll 

        Returns: bool True if it is a Spare, False if not
        '''
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        '''
        Calculates score of a Strike
            
            args:
                rollIndex(int): the index number of the roll 

            Returns: 
                (int): sum of Strike frame score and next two rolls
        '''
        return  10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        '''
        Calculates score of a Spare
            
            args:
                rollIndex(int): the index number of the roll 

            Returns: 
                (int): sum of Spare frame score and next rolls
        '''
        return  10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        '''
        Calculates score of a Frame
            
            args:
                rollIndex(int): the index number of the roll 

            Returns: 
                (int): sum of both rolls in frame
        '''
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.