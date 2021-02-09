import unittest
from on_server_learning.algorithms_1.trees.deep_and_wide_all_nodes import *


class Test_BST(unittest.TestCase):

    def test_deep_0(self):
        tree = BST(None)
        Child_1 = (10, 10)
        Child_2 = (4, 4)
        Child_3 = (2, 2)
        Child_4 = (6, 6)
        Child_5 = (20, 20)
        Child_6 = (14, 14)
        Child_7 = (12, 12)
        Child_8 = (17, 17)
        Child_10 = (25, 25)
        Child_11 = (23, 23)
        Child_14 = (28, 28)
        self.assertTrue(tree.AddKeyValue(Child_1[0], Child_1[1]))
        self.assertTrue(tree.AddKeyValue(Child_2[0], Child_2[1]))
        self.assertTrue(tree.AddKeyValue(Child_3[0], Child_3[1]))
        self.assertTrue(tree.AddKeyValue(Child_4[0], Child_4[1]))
        self.assertTrue(tree.AddKeyValue(Child_5[0], Child_5[1]))
        self.assertTrue(tree.AddKeyValue(Child_6[0], Child_6[1]))
        self.assertTrue(tree.AddKeyValue(Child_7[0], Child_7[1]))
        self.assertTrue(tree.AddKeyValue(Child_8[0], Child_8[1]))
        self.assertTrue(tree.AddKeyValue(Child_10[0], Child_10[1]))
        self.assertTrue(tree.AddKeyValue(Child_11[0], Child_11[1]))
        self.assertTrue(tree.AddKeyValue(Child_14[0], Child_14[1]))
        arrow_nodes = [tree.Root.LeftChild.LeftChild, tree.Root.LeftChild, tree.Root.LeftChild.RightChild,  tree.Root,
                       tree.Root.RightChild.LeftChild.LeftChild, tree.Root.RightChild.LeftChild,
                       tree.Root.RightChild.LeftChild.RightChild, tree.Root.RightChild,
                       tree.Root.RightChild.RightChild.LeftChild,
                       tree.Root.RightChild.RightChild, tree.Root.RightChild.RightChild.RightChild]
        self.assertEqual(tree.DeepAllNodes(0), arrow_nodes)

    def test_deep_1(self):
        tree = BST(None)
        Child_1 = (10, 10)
        Child_2 = (4, 4)
        Child_3 = (2, 2)
        Child_4 = (6, 6)
        Child_5 = (20, 20)
        Child_6 = (14, 14)
        Child_7 = (12, 12)
        Child_8 = (17, 17)
        Child_10 = (25, 25)
        Child_11 = (23, 23)
        Child_14 = (28, 28)
        self.assertTrue(tree.AddKeyValue(Child_1[0], Child_1[1]))
        self.assertTrue(tree.AddKeyValue(Child_2[0], Child_2[1]))
        self.assertTrue(tree.AddKeyValue(Child_3[0], Child_3[1]))
        self.assertTrue(tree.AddKeyValue(Child_4[0], Child_4[1]))
        self.assertTrue(tree.AddKeyValue(Child_5[0], Child_5[1]))
        self.assertTrue(tree.AddKeyValue(Child_6[0], Child_6[1]))
        self.assertTrue(tree.AddKeyValue(Child_7[0], Child_7[1]))
        self.assertTrue(tree.AddKeyValue(Child_8[0], Child_8[1]))
        self.assertTrue(tree.AddKeyValue(Child_10[0], Child_10[1]))
        self.assertTrue(tree.AddKeyValue(Child_11[0], Child_11[1]))
        self.assertTrue(tree.AddKeyValue(Child_14[0], Child_14[1]))
        arrow_nodes = [tree.Root.LeftChild.LeftChild, tree.Root.LeftChild.RightChild, tree.Root.LeftChild,
                       tree.Root.RightChild.LeftChild.LeftChild, tree.Root.RightChild.LeftChild.RightChild,
                       tree.Root.RightChild.LeftChild, tree.Root.RightChild.RightChild.LeftChild,
                       tree.Root.RightChild.RightChild.RightChild, tree.Root.RightChild.RightChild,
                       tree.Root.RightChild, tree.Root]
        self.assertEqual(tree.DeepAllNodes(1), arrow_nodes)

    def test_deep_2(self):
        tree = BST(None)
        Child_1 = (10, 10)
        Child_2 = (4, 4)
        Child_3 = (2, 2)
        Child_4 = (6, 6)
        Child_5 = (20, 20)
        Child_6 = (14, 14)
        Child_7 = (12, 12)
        Child_8 = (17, 17)
        Child_10 = (25, 25)
        Child_11 = (23, 23)
        Child_14 = (28, 28)
        self.assertTrue(tree.AddKeyValue(Child_1[0], Child_1[1]))
        self.assertTrue(tree.AddKeyValue(Child_2[0], Child_2[1]))
        self.assertTrue(tree.AddKeyValue(Child_3[0], Child_3[1]))
        self.assertTrue(tree.AddKeyValue(Child_4[0], Child_4[1]))
        self.assertTrue(tree.AddKeyValue(Child_5[0], Child_5[1]))
        self.assertTrue(tree.AddKeyValue(Child_6[0], Child_6[1]))
        self.assertTrue(tree.AddKeyValue(Child_7[0], Child_7[1]))
        self.assertTrue(tree.AddKeyValue(Child_8[0], Child_8[1]))
        self.assertTrue(tree.AddKeyValue(Child_10[0], Child_10[1]))
        self.assertTrue(tree.AddKeyValue(Child_11[0], Child_11[1]))
        self.assertTrue(tree.AddKeyValue(Child_14[0], Child_14[1]))
        arrow_nodes = [tree.Root, tree.Root.LeftChild, tree.Root.LeftChild.LeftChild, tree.Root.LeftChild.RightChild,
                       tree.Root.RightChild, tree.Root.RightChild.LeftChild, tree.Root.RightChild.LeftChild.LeftChild,
                       tree.Root.RightChild.LeftChild.RightChild, tree.Root.RightChild.RightChild,
                       tree.Root.RightChild.RightChild.LeftChild, tree.Root.RightChild.RightChild.RightChild]
        self.assertEqual(tree.DeepAllNodes(2), arrow_nodes)

    def test_wide(self):
        tree = BST(None)
        Child_1 = (10, 10)
        Child_2 = (4, 4)
        Child_3 = (2, 2)
        Child_4 = (6, 6)
        Child_5 = (20, 20)
        Child_6 = (14, 14)
        Child_7 = (12, 12)
        Child_8 = (17, 17)
        Child_10 = (25, 25)
        Child_11 = (23, 23)
        Child_14 = (28, 28)
        self.assertTrue(tree.AddKeyValue(Child_1[0], Child_1[1]))
        self.assertTrue(tree.AddKeyValue(Child_2[0], Child_2[1]))
        self.assertTrue(tree.AddKeyValue(Child_3[0], Child_3[1]))
        self.assertTrue(tree.AddKeyValue(Child_4[0], Child_4[1]))
        self.assertTrue(tree.AddKeyValue(Child_5[0], Child_5[1]))
        self.assertTrue(tree.AddKeyValue(Child_6[0], Child_6[1]))
        self.assertTrue(tree.AddKeyValue(Child_7[0], Child_7[1]))
        self.assertTrue(tree.AddKeyValue(Child_8[0], Child_8[1]))
        self.assertTrue(tree.AddKeyValue(Child_10[0], Child_10[1]))
        self.assertTrue(tree.AddKeyValue(Child_11[0], Child_11[1]))
        self.assertTrue(tree.AddKeyValue(Child_14[0], Child_14[1]))
        arrow_nodes = [tree.Root, tree.Root.LeftChild, tree.Root.RightChild, tree.Root.LeftChild.LeftChild,
                       tree.Root.LeftChild.RightChild, tree.Root.RightChild.LeftChild, tree.Root.RightChild.RightChild,
                       tree.Root.RightChild.LeftChild.LeftChild, tree.Root.RightChild.LeftChild.RightChild,
                       tree.Root.RightChild.RightChild.LeftChild, tree.Root.RightChild.RightChild.RightChild]
        self.assertEqual(tree.WideAllNodes(), arrow_nodes)


if __name__ == '__main__':
    unittest.main()
