import unittest
from on_server_learning.algorithms_1.trees.aBST import *


class Test_BST(unittest.TestCase):

    def test_AddKey(self):
        tree = aBST(2)
        self.assertEqual(tree.Tree, [None, None, None, None, None, None, None])
        self.assertEqual(len(tree.Tree), 7)
        Child_1 = 10
        Child_2 = 4
        Child_3 = 2
        Child_4 = 6
        Child_5 = 20
        Child_6 = 14
        Child_7 = 25
        self.assertEqual(tree.FindKeyIndex(Child_1), 0)
        self.assertEqual(tree.AddKey(Child_1), 0)
        self.assertEqual(tree.Tree, [10, None, None, None, None, None, None])
        self.assertEqual(tree.FindKeyIndex(Child_2), -1)
        self.assertEqual(tree.AddKey(Child_2), 1)
        self.assertEqual(tree.Tree, [10, 4, None, None, None, None, None])
        self.assertEqual(tree.FindKeyIndex(Child_3), -3)
        self.assertEqual(tree.AddKey(Child_3), 3)
        self.assertEqual(tree.Tree, [10, 4, None, 2, None, None, None])
        self.assertEqual(tree.FindKeyIndex(Child_4), -4)
        self.assertEqual(tree.AddKey(Child_4), 4)
        self.assertEqual(tree.Tree, [10, 4, None, 2, 6, None, None])
        self.assertEqual(tree.FindKeyIndex(Child_5), -2)
        self.assertEqual(tree.AddKey(Child_5), 2)
        self.assertEqual(tree.Tree, [10, 4, 20, 2, 6, None, None])
        self.assertEqual(tree.FindKeyIndex(Child_6), -5)
        self.assertEqual(tree.AddKey(Child_6), 5)
        self.assertEqual(tree.Tree, [10, 4, 20, 2, 6, 14, None])
        self.assertEqual(tree.FindKeyIndex(Child_7), -6)
        self.assertEqual(tree.AddKey(Child_7), 6)
        self.assertEqual(tree.Tree, [10, 4, 20, 2, 6, 14, 25])
        self.assertEqual(tree.AddKey(10), 0)
        self.assertEqual(tree.AddKey(6), 4)
        self.assertEqual(tree.AddKey(45), -1)
        self.assertIsNone(tree.FindKeyIndex(45))


if __name__ == '__main__':
    unittest.main()
