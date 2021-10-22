from random import randint
class Dice:
    def __init__(self, numFaces):
        self.numFaces = numFaces
    def roll(self):
        return randint(1, self.numFaces)
        