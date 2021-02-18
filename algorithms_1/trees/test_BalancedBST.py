import unittest
from on_server_learning.algorithms_1.trees.BalancedBST import *


class Test_BST(unittest.TestCase):

    def test_add_and_find(self):
        array_not_sorted = [5, 2, 3, 4, 1, 0]
        tree_balance = BalancedBST()
        tree_balance.GenerateTree(array_not_sorted)
        self.assertEqual(tree_balance.Root.NodeKey, 3)  # Проверка добавления Root
        self.assertEqual(tree_balance.Root.Level, 1)
        self.assertEqual(tree_balance.Root.LeftChild.NodeKey, 1)  # Проверка значения LeftChild
        self.assertEqual(tree_balance.Root.LeftChild.Level, 2)
        self.assertEqual(tree_balance.Root.RightChild.NodeKey, 5)  # Проверка значения RightChild
        self.assertEqual(tree_balance.Root.RightChild.Level, 2)
        self.assertEqual(tree_balance.Root.LeftChild.Parent.NodeKey, 3)  # Проверка значения LeftChild
        self.assertEqual(tree_balance.Root.RightChild.Parent.NodeKey, 3)  # Проверка значения RightChild
        self.assertEqual(tree_balance.Root.LeftChild.LeftChild.NodeKey, 0)
        self.assertEqual(tree_balance.Root.LeftChild.LeftChild.Level, 3)
        self.assertEqual(tree_balance.Root.LeftChild.LeftChild.LeftChild, None)
        self.assertEqual(tree_balance.Root.LeftChild.LeftChild.RightChild, None)
        self.assertEqual(tree_balance.Root.LeftChild.LeftChild.Parent.NodeKey, 1)
        self.assertEqual(tree_balance.Root.LeftChild.RightChild.NodeKey, 2)
        self.assertEqual(tree_balance.Root.LeftChild.RightChild.Level, 3)
        self.assertEqual(tree_balance.Root.LeftChild.RightChild.RightChild, None)
        self.assertEqual(tree_balance.Root.LeftChild.RightChild.LeftChild, None)
        self.assertEqual(tree_balance.Root.LeftChild.RightChild.Parent.NodeKey, 1)
        self.assertEqual(tree_balance.Root.RightChild.LeftChild.NodeKey, 4)
        self.assertEqual(tree_balance.Root.RightChild.LeftChild.Level, 3)
        self.assertEqual(tree_balance.Root.RightChild.LeftChild.RightChild, None)
        self.assertEqual(tree_balance.Root.RightChild.LeftChild.LeftChild, None)
        self.assertEqual(tree_balance.Root.RightChild.LeftChild.Parent.NodeKey, 5)
        self.assertEqual(tree_balance.Root.RightChild.RightChild, None)
        self.assertTrue(tree_balance.IsBalanced(tree_balance.Root))
        tree_balance.Root.LeftChild.LeftChild.LeftChild = BSTNode(-1, tree_balance.Root.LeftChild.LeftChild)
        tree_balance.Root.LeftChild.LeftChild.LeftChild.Level = 4
        tree_balance.Root.LeftChild.LeftChild.LeftChild.LeftChild = BSTNode(-2, tree_balance.Root.LeftChild.LeftChild.LeftChild)
        tree_balance.Root.LeftChild.LeftChild.LeftChild.LeftChild.Level = 5
        self.assertFalse(tree_balance.IsBalanced(tree_balance.Root))


if __name__ == '__main__':
    unittest.main()
