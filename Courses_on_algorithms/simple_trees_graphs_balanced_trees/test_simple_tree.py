import unittest
from on_server_learning.algorithms_1.trees.simple_tree import *
import collections


class Test_SimpleTree(unittest.TestCase):

    def test_AddChild(self):
        tree = SimpleTree(None)
        child_1 = SimpleTreeNode(1, None)
        tree.AddChild(None, child_1)
        self.assertEqual(tree.Count(), 1)
        self.assertEqual(tree.Root.NodeValue, 1)

    def test_AddChild_2(self):
        array_1 = []
        array_2 = []
        tree = SimpleTree(None)
        child_1 = SimpleTreeNode(1, None)
        child_2 = SimpleTreeNode(2, None)
        child_3 = SimpleTreeNode(3, None)
        child_4 = SimpleTreeNode(4, None)
        child_5 = SimpleTreeNode(5, None)
        tree.AddChild(None, child_1)
        tree.AddChild(child_1, child_2)
        tree.AddChild(child_2, child_3)
        tree.AddChild(child_2, child_4)
        tree.AddChild(child_1, child_5)
        array_1.append(child_2)
        array_1.append(child_5)
        array_2.append(child_3)
        array_2.append(child_4)
        self.assertEqual(tree.Count(), 5)
        self.assertEqual(tree.Root.Children, array_1)
        self.assertEqual(tree.Root.Children[0].Children, array_2)

    def test_DeleteNode(self):
        array_1 = []
        tree = SimpleTree(None)
        child_1 = SimpleTreeNode(1, None)
        child_2 = SimpleTreeNode(2, None)
        child_3 = SimpleTreeNode(3, None)
        child_4 = SimpleTreeNode(4, None)
        child_5 = SimpleTreeNode(5, None)
        tree.AddChild(None, child_1)
        tree.AddChild(child_1, child_2)
        tree.AddChild(child_2, child_3)
        tree.AddChild(child_2, child_4)
        tree.AddChild(child_1, child_5)
        array_1.append(child_5)
        tree.DeleteNode(child_2)
        self.assertEqual(tree.Count(), 2)
        self.assertEqual(tree.Root.Children, array_1)

    def test_DeleteNode_leaf(self):
        array_1 = []
        tree = SimpleTree(None)
        child_1 = SimpleTreeNode(1, None)
        child_2 = SimpleTreeNode(2, None)
        child_3 = SimpleTreeNode(3, None)
        child_4 = SimpleTreeNode(4, None)
        child_5 = SimpleTreeNode(5, None)
        tree.AddChild(None, child_1)
        tree.AddChild(child_1, child_2)
        tree.AddChild(child_2, child_3)
        tree.AddChild(child_2, child_4)
        tree.AddChild(child_1, child_5)
        array_1.append(child_2)
        tree.DeleteNode(child_5)
        self.assertEqual(tree.Count(), 4)
        self.assertEqual(tree.Root.Children, array_1)

    def test_GetAllNodes(self):
        array_1 = []
        tree = SimpleTree(None)
        child_1 = SimpleTreeNode(1, None)
        child_2 = SimpleTreeNode(2, None)
        child_3 = SimpleTreeNode(3, None)
        child_4 = SimpleTreeNode(4, None)
        child_5 = SimpleTreeNode(5, None)
        tree.AddChild(None, child_1)
        tree.AddChild(child_1, child_2)
        tree.AddChild(child_2, child_3)
        tree.AddChild(child_2, child_4)
        tree.AddChild(child_1, child_5)
        array_1.append(child_1)
        array_1.append(child_2)
        array_1.append(child_3)
        array_1.append(child_4)
        array_1.append(child_5)
        array_2 = tree.GetAllNodes()
        res = [x for x in array_1 + array_2 if x not in array_1 or x not in array_2]
        flag = False
        if collections.Counter(array_1) == collections.Counter(array_1):
            flag = True
        self.assertEqual(res, [])
        self.assertTrue(flag)

    def test_FindNodesByValue(self):
        array_1 = []
        tree = SimpleTree(None)
        child_1 = SimpleTreeNode(1, None)
        child_2 = SimpleTreeNode(2, None)
        child_3 = SimpleTreeNode(3, None)
        child_4 = SimpleTreeNode(4, None)
        child_5 = SimpleTreeNode(5, None)
        tree.AddChild(None, child_1)
        tree.AddChild(child_1, child_2)
        tree.AddChild(child_2, child_3)
        tree.AddChild(child_2, child_4)
        tree.AddChild(child_1, child_5)
        array_1.append(child_2)
        array_2 = tree.FindNodesByValue(2)
        self.assertEqual(tree.Count(), 5)
        self.assertEqual(array_2, array_1)

    def test_MoveNode(self):
        array_1 = []
        array_2 = []
        tree = SimpleTree(None)
        child_1 = SimpleTreeNode(1, None)
        child_2 = SimpleTreeNode(2, None)
        child_3 = SimpleTreeNode(3, None)
        child_4 = SimpleTreeNode(4, None)
        child_5 = SimpleTreeNode(5, None)
        tree.AddChild(None, child_1)
        tree.AddChild(child_1, child_2)
        tree.AddChild(child_2, child_3)
        tree.AddChild(child_2, child_4)
        tree.AddChild(child_1, child_5)
        tree.MoveNode(child_2, child_5)
        array_1.append(child_5)
        array_2.append(child_2)
        self.assertEqual(tree.Count(), 5)
        self.assertEqual(tree.Root.Children, array_1)
        self.assertEqual(tree.Root.Children[0].Children, array_2)

    def test_LeafCount(self):
        tree = SimpleTree(None)
        child_1 = SimpleTreeNode(1, None)
        child_2 = SimpleTreeNode(2, None)
        child_3 = SimpleTreeNode(3, None)
        child_4 = SimpleTreeNode(4, None)
        child_5 = SimpleTreeNode(5, None)
        tree.AddChild(None, child_1)
        tree.AddChild(child_1, child_2)
        tree.AddChild(child_2, child_3)
        tree.AddChild(child_2, child_4)
        tree.AddChild(child_1, child_5)
        self.assertEqual(tree.LeafCount(), 3)


if __name__ == '__main__':
    unittest.main()
