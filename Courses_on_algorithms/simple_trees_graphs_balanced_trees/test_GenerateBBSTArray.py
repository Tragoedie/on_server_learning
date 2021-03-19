import unittest
from on_server_learning.algorithms_1.trees.GenerateBBSTArray import *


class Test_BST(unittest.TestCase):

    def test_root(self):
        array = [1]
        self.assertEqual(GenerateBBSTArray(array), [1, None, None])

    def test_root_left(self):
        array = [1, 0]
        self.assertEqual(GenerateBBSTArray(array), [1, 0, None])

    def test_root_right(self):
        array = [3, 1, 0]
        self.assertEqual(GenerateBBSTArray(array), [1, 0, 3])

    def test_array(self):
        array = [5, 6, 2, 1, 3, 0, 4, 7, 8]
        self.assertEqual(GenerateBBSTArray(array), [4, 2, 7, 1, 3, 6, 8, 0, None, None, None, 5, None, None, None])

    def array_none(self):
        array = []
        self.assertEqual(GenerateBBSTArray(array), [None, None, None])


if __name__ == '__main__':
    unittest.main()
