import statistics
from StatsticOperations.mean import Mean
from StatsticOperations.median import Median
from StatsticOperations.standardDeviation import StandardDeviation

class Skewness:
    @staticmethod
    def Skew(alist):
        mean = Mean.Mean1(alist)
        median = Median.Median1(alist)
        stD = StandardDeviation.StandardDeviation1(alist)
        skew = 3 * (mean - median)/stD
        return skew