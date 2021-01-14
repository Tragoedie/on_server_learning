import unittest
from on_server_learning.algorithms_1.ordered_list.ordered_list import *


class Test_ordered_list(unittest.TestCase):

    def test_add_head_true(self):
        ord_list = OrderedList(True)
        for i in range(1, 10, 2):
            ord_list.add(i)
        ord_list.add(0)
        self.assertEqual(ord_list.len(), 6)
        self.assertEqual(ord_list.head.value, 0)

    def test_add_middle_true(self):
        ord_list = OrderedList(True)
        for i in range(1, 10, 2):
            ord_list.add(i)
        ord_list.add(4)
        node = ord_list.head
        for j in range(2):
            node = node.next
        self.assertEqual(ord_list.len(), 6)
        self.assertEqual(node.value, 4)

    def test_add_tail_true(self):
        ord_list = OrderedList(True)
        for i in range(1, 10, 2):
            ord_list.add(i)
        ord_list.add(10)
        self.assertEqual(ord_list.len(), 6)
        self.assertEqual(ord_list.tail.value, 10)

    def test_add_head_false(self):
        ord_list = OrderedList(False)
        for i in range(1, 10, 2):
            ord_list.add(i)
        ord_list.add(10)
        self.assertEqual(ord_list.len(), 6)
        self.assertEqual(ord_list.head.value, 10)

    def test_add_middle_false(self):
        ord_list = OrderedList(False)
        for i in range(9, 0, -2):
            ord_list.add(i)
        ord_list.add(4)
        node = ord_list.head
        for j in range(3):
            node = node.next
        self.assertEqual(ord_list.len(), 6)
        self.assertEqual(node.value, 4)

    def test_add_tail_false(self):
        ord_list = OrderedList(False)
        for i in range(9, 0, -2):
            ord_list.add(i)
        ord_list.add(0)
        self.assertEqual(ord_list.len(), 6)
        self.assertEqual(ord_list.tail.value, 0)


    def test_find_head(self):
        ord_list = OrderedList(True)
        for i in range(1, 10, 2):
            ord_list.add(i)
        numb = ord_list.find(1)
        self.assertEqual(numb, ord_list.head)

    def test_find_tail(self):
        ord_list = OrderedList(False)
        for i in range(1, 10, 2):
            ord_list.add(i)
        numb = ord_list.find(1)
        self.assertEqual(numb, ord_list.tail)

    def test_find_middle(self):
        ord_list = OrderedList(False)
        for i in range(1, 10, 2):
            ord_list.add(i)
        numb = ord_list.find(5)
        node = ord_list.head
        for j in range(2):
            node = node.next
        self.assertEqual(numb, node)

    def test_find_none(self):
        ord_list = OrderedList(True)
        for i in range(1, 10, 2):
            ord_list.add(i)
        self.assertIsNone(ord_list.find(4))


if __name__ == '__main__':
    unittest.main()
