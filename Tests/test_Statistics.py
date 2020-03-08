import unittest

from StatsticOperations import mean
from StatsticOperations import median
from StatsticOperations import mode

class MyStatsCase(unittest.TestCase):

    def test_StatisticOperations_Mean(self):
        aList = [1,2,3,4]
        return mean.Mean.Mean1(aList)

    def test_StatsticOperations_Median(self):
        aList = [1,2,3,4]
        return median.Median.Median1(aList)

    def test_StatisticOperations_Mode(self):
        aList = [1,2,2,3,4]
        return mode.Mode.Mode1(aList)

