import unittest
from on_server_learning.Courses_on_algorithms.algorithms_of_sorting.BinarySearch import BinarySearch


class Test_Deque(unittest.TestCase):

    def testSearch_1(self):
        bin_search = BinarySearch([])
        bin_search.Step(1)
        self.assertEqual(bin_search.GetResult(), -1)

    def testSearch_2(self):
        array = [1, 3, 4]
        bin_search = BinarySearch(array)
        while bin_search.GetResult() == 0:
            bin_search.Step(2)
        self.assertEqual(bin_search.GetResult(), -1)

    def testSearch_3(self):
        bin_search = BinarySearch([1, 2])
        while bin_search.GetResult() == 0:
            bin_search.Step(3)
        self.assertEqual(bin_search.GetResult(), -1)

    def testSearch_4(self):
        bin_search = BinarySearch([1])
        bin_search.Step(1)
        self.assertEqual(bin_search.GetResult(), 1)

    def testSearch_5(self):
        array = [i for i in range(30)]
        bin_search = BinarySearch(array)
        bin_search.Step(25)
        while bin_search.GetResult() == 0:
            bin_search.Step(25)
        self.assertEqual(bin_search.GetResult(), 1)
        bin_search = BinarySearch(array)
        while bin_search.GetResult() == 0:
            bin_search.Step(15)
        self.assertEqual(bin_search.GetResult(), 1)
        bin_search = BinarySearch(array)
        while bin_search.GetResult() == 0:
            bin_search.Step(31)
        self.assertEqual(bin_search.GetResult(), -1)
        bin_search = BinarySearch(array)
        while bin_search.GetResult() != 1:
            bin_search.Step(2)
        self.assertEqual(bin_search.GetResult(), 1)

    def testSearch_6(self):
        array = [i for i in range(1, 100)]
        bin_search = BinarySearch(array)
        self.assertEqual(bin_search.Left, 0)
        self.assertEqual(bin_search.Right, 98)
        self.assertEqual(bin_search.GetResult(), 0)
        bin_search.Step(49)
        self.assertEqual(bin_search.Left, 0)
        self.assertEqual(bin_search.Right, 48)
        self.assertEqual(bin_search.GetResult(), 0)
        bin_search.Step(49)
        self.assertEqual(bin_search.Left, 25)
        self.assertEqual(bin_search.Right, 48)
        self.assertEqual(bin_search.GetResult(), 0)
        bin_search.Step(49)
        self.assertEqual(bin_search.Left, 37)
        self.assertEqual(bin_search.Right, 48)
        self.assertEqual(bin_search.GetResult(), 0)
        bin_search.Step(49)
        self.assertEqual(bin_search.Left, 43)
        self.assertEqual(bin_search.Right, 48)
        self.assertEqual(bin_search.GetResult(), 0)
        bin_search.Step(49)
        self.assertEqual(bin_search.Left, 46)
        self.assertEqual(bin_search.Right, 48)
        self.assertEqual(bin_search.GetResult(), 0)
        bin_search.Step(49)
        self.assertEqual(bin_search.Left, 48)
        self.assertEqual(bin_search.Right, 48)
        self.assertEqual(bin_search.GetResult(), 1)


if __name__ == '__main__':
    unittest.main()
