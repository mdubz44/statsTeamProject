from StatsticOperations.mean import Mean
from StatsticOperations.standardDeviation import StandardDeviation

class ZScore:

    @staticmethod
    def ZScore1(alist):
        mean = Mean.Mean1(alist)
        stD = StandardDeviation.StandardDeviation1(alist)
        zScoreList = []
        for i in alist:
            zscore = (i - mean) / stD
            zScoreList.append(zscore)
        return zScoreList