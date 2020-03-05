from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from StatsticOperations.mean import Mean
from StatsticOperations.median import Median


class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Mean(self):
        aList = [1,2,3,4]
        self.Result = Mean.Mean1(aList)
        return self.Result

    def Median(self):
        aList = [1,2,3,4]
        self.Result = Median.Median1(aList)
        return self.Result