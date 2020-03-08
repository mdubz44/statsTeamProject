import unittest

from StatsticOperations.mean import Mean
from StatsticOperations.median import Median
from StatsticOperations.mode import Mode
from StatsticOperations.variance import Variance
from StatsticOperations.standardDeviation import StandardDeviation

class MyStatsCase(unittest.TestCase):

    def test_StatisticOperations_Mean(self):
        aList = [1,2,3,4]
        return Mean.Mean1(aList)

    def test_StatsticOperations_Median(self):
        aList = [1,2,3,4]
        return Median.Median1(aList)

    def test_StatisticOperations_Mode(self):
        aList = [1,2,2,3,4]
        return Mode.Mode1(aList)

    def test_StatisticOperations_Variance(self):
        aList = [1,2,3,4]
        mean = Mean.Mean1(aList)
        return  Variance.Variance1(aList)

    def testStatisticOperations_StandardDeviation(self):
        aList = [1,2,3,4]
        return StandardDeviation.StandardDeviation1(aList)
