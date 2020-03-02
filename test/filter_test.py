import unittest
from src.filter import TemporalFilter, RangeFilter


class TemporalRangeTest(unittest.TestCase):

    def test_update(self):
        filter_object = TemporalFilter(n=5, d=3)
        self.assertEqual([0, 1, 2, 1, 3], filter_object.update(scan=[0, 1, 2, 1, 3]))
        self.assertEqual([0.5, 3, 4.5, 1, 3], filter_object.update(scan=[1, 5, 7, 1, 3]))
        self.assertEqual([1, 3, 4, 1, 3], filter_object.update(scan=[2, 3, 4, 1, 0]))
        self.assertEqual([1.5, 3, 3.5, 1, 3], filter_object.update(scan=[3,3,3,1,3]))
        self.assertEqual([2.5, 3, 4, 1, 1.5], filter_object.update(scan=[10, 2, 4, 0, 0]))

    def test_update_n7_d4(self):
        filter_object = TemporalFilter(n=7, d=4)
        self.assertEqual([0, 1, 2, 1, 51, 60, 3], filter_object.update(scan=[0, 1, 2, 1, 51, 60, 3]))
        self.assertEqual([5.0, 3.5, 3.0, 1.0, 31.0, 75.0, 1.502], filter_object.update(scan=[10, 6, 4, 1, 11, 90, 0.004]))
        self.assertEqual([1, 6, 3, 1, 11, 60, 3], filter_object.update(scan=[1, 8, 3, 0.003, 0.03, 1, 84]))
        self.assertEqual([0.55, 7.0, 3.5, 1.0, 8.0, 75.0, 1.502], filter_object.update(scan=[0.1, 13, 8, 1, 5, 96, 0.0007]))
        self.assertEqual([1, 6, 3, 1, 10, 90, 0.2], filter_object.update(scan=[84, 0, 3, 19, 10, 99, 0.2]))


class RangeUpdate(unittest.TestCase):

    def test_range(self):
        filter_range=RangeFilter()
        self.assertEqual([0.03, 1, 2, 1, 50], filter_range.update(scan=[0, 1, 2, 1, 51]))
        self.assertEqual([1, 5, 50, 1, 3], filter_range.update(scan=[1, 5, 70, 1, 3]))
        self.assertEqual([2, 3, 4, 1, 0.03], filter_range.update(scan=[2, 3, 4, 1, 0.0001]))
        self.assertEqual([3, 50, 3, 1, 3], filter_range.update(scan=[3, 300, 3, 1, 3]))
        self.assertEqual([10, 2, 4, 0.03, 0.03], filter_range.update(scan=[10, 2, 4, 0.000005, 0]))

    def test_range_n7_d4(self):
        filter_range = RangeFilter()
        self.assertEqual([0.03, 1, 2, 1, 50, 9, 11], filter_range.update(scan=[0, 1, 2, 1, 60, 9, 11]))
        self.assertEqual([1, 5, 50, 0.03, 3, 9, 10], filter_range.update(scan=[1, 5, 70, 0.0005, 3, 9, 10]))
        self.assertEqual([2, 50, 4, 1, 0.03, 0.03, 11], filter_range.update(scan=[2, 67, 4, 1, 0.0001, 0.005, 11]))
        self.assertEqual([3, 50, 3, 1, 3, 0.04, 0.05], filter_range.update(scan=[3, 600, 3, 1, 3, 0.04, 0.05]))
        self.assertEqual([10, 2, 4, 0.03, 0.03, 50, 50], filter_range.update(scan=[10, 2, 4, 0.000005, 0, 70, 87]))


if __name__ == "__main__":
    unittest.main()
