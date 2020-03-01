from abc import ABCMeta, abstractmethod


class Filter(object):

    __metaclass__ = ABCMeta

    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.last_d = [[] for _ in range(self.n)]

    @abstractmethod
    def update(self, scan):
        pass


class RangeFilter(Filter):

    range_min = 0.03
    range_max = 50

    def __init__(self, n, d):
        super(RangeFilter, self).__init__(n, d)

    def update(self, scan):

        filtered_scan = []

        for scan_value in scan:
            if scan_value < 0.03:
                filtered_scan.append(0.03)
            elif scan_value > 50:
                filtered_scan.append(50)
            else:
                filtered_scan.append(scan_value)

        return filtered_scan


class TemporalFilter(Filter):

    def __init__(self, n, d):
        super(TemporalFilter, self).__init__(n, d)

    @staticmethod
    def median(lst):
        n = len(lst)
        s = sorted(lst)
        return (sum(s[n // 2 - 1:n // 2 + 1]) / 2.0, s[n // 2])[n % 2] if n else None

    def update(self, scan):

        medians = []

        for i, scan_value in enumerate(scan):
            self.last_d[i].append(scan_value)
            self.last_d[i] = self.last_d[i][-(self.d+1):]
            medians.append(self.median(self.last_d[i]))

        return medians


obj = RangeFilter(n=5, d=3)
# print obj.update(scan=[0, 1, 2, 1, 51])
# print obj.update(scan=[1, 5, 7, 1, 3])
# print obj.update(scan=[2, 3, 4, 1, 0])
# print obj.update(scan=[3, 3, 3, 1, 3])
# print obj.update(scan=[10, 2, 4, 0, 0])
