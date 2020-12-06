import unittest
from on_server_learning.Iteration.List2_1 import List2_1


class List2_1_tests(unittest.TestCase):

    def test_List2_1_1(self):
        massive = []
        self.l2_1 = List2_1(5)
        for i in self.l2_1:
            massive.append(i)
        self.assertEqual(massive, [5, 10, 20, 40, 80, 160, 320, 640, 1280])

    def test_List2_1_2(self):
        massive = []
        self.l2_1 = List2_1(0)
        for i in self.l2_1:
            massive.append(i)
        self.assertEqual(massive, [0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_List2_1_3(self):
        massive = []
        self.l2_1 = List2_1(10000000000)
        for i in self.l2_1:
            massive.append(i)
        self.assertEqual(massive, [10000000000, 20000000000, 40000000000, 80000000000, 160000000000,
                                   320000000000, 640000000000, 1280000000000, 2560000000000])


if __name__ == '__main__':
    unittest.main()