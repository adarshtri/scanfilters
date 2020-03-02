from abc import ABCMeta, abstractmethod
import numpy as np
np.set_printoptions(suppress=True)
class Filter(object):

    __metaclass__ = ABCMeta

    def __init__(self, n=None, d=None):
        self.n = n
        self.d = d
        if self.n is not None:
            self.last_d = [[] for _ in range(self.n)]
        else:
            self.last_d = None

    @abstractmethod
    def update(self, scan):
        pass


class RangeFilter(Filter):

    range_min = 0.03
    range_max = 50

    def __init__(self):
        super(RangeFilter, self).__init__()

    def update(self, scan):

        filtered_scan = []
        #filtered_scan = np.array(a)

        scan=np.array(scan)
        return np.where(scan<=0.03,0.03-scan, 0)+scan+np.where(scan>=50,50-scan,0)
        # for scan_value in scan:
        #     if scan_value < 0.03:
        #         filtered_scan.append(0.03)
        #     elif scan_value > 50:
        #         filtered_scan.append(50)
        #     else:
        #         filtered_scan.append(scan_value)
        #
        # return filtered_scan


class TemporalFilter(Filter):

    def __init__(self, n, d):
        super(TemporalFilter, self).__init__(n, d)
        self.data=[]

    @staticmethod
    def median(lst):
        n = len(lst)
        s = sorted(lst)
        return (sum(s[n // 2 - 1:n // 2 + 1]) / 2.0, s[n // 2])[n % 2] if n else None

    def update(self, scan):

        medians = []

        self.data.append(scan)
        return list(np.median(np.array(self.data[-4:]),axis=0))
        #print(scan)
        # for i, scan_value in enumerate(scan):
        #     #print(i)
        #     self.last_d[i].append(scan_value)
        #     self.last_d[i] = self.last_d[i][-(self.d+1):]
        #     medians.append(self.median(self.last_d[i]))
        #
        # return medians

# filter_object=TemporalFilter(n=5,d=3)
# print filter_object.update(scan=[1,10,98,0.03,1])
# print filter_object.update(scan=[0,11,56,0,1])