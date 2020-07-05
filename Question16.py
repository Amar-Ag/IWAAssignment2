"""
16. Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player.
"""


class Chess:
    def __init__(self, playercount, magicNumber):
        self.playercount = playercount
        self.magicNumber = magicNumber  # Number that takes a coin out
        self.goHomeBeforeCut = False
        self.askBeforeCut = False

    @staticmethod
    def turnCalculator(self):
        for i in self.playercount:
            pass  # calculate turn

    @staticmethod
    def rulesSetter(self, goHomeBeforeCut, askBeforeCut):
        self.goHomeBeforeCut = goHomeBeforeCut
        self.askBeforeCut = askBeforeCut

    def rollDice(self):
        pass

    def calculatePath(self, diceValue, player):
        pass

    def starValues(self):
        pass

    def goHome(self):
        pass

    def cutOpponent(self,opponentPosition):
        pass
