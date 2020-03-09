from StatsticOperations.median import Median
import statistics


class Quartile:

    @staticmethod
    def Quartile1(aList):
        med = Median.Median1(aList)
        q1 = Median.Median1(aList[0:med])
        q3 = Median.Median1(aList[med:-1])
        return q1, med, q3