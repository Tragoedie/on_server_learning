import unittest
from on_server_learning.algorithms_1.linked_list.linked_list_with_dummy_3 import Node
from on_server_learning.algorithms_1.linked_list.linked_list_with_dummy_3 import LinkedList2


class Test_LinkedList2_with_dummy(unittest.TestCase):

    def test_add_in_head_fake_function(self):
        s_list = LinkedList2()
        s_list.add_in_head(Node(55))
        self.assertEqual(s_list.head.value, 55)
        self.assertEqual(s_list.tail.value, 55)
        self.assertEqual(s_list.head, s_list.tail)

    def test_add_in_tail_fake_function(self):
        s_list = LinkedList2()
        s_list.add_in_tail(Node(11))
        s_list.add_in_tail(Node(22))
        s_list.add_in_tail(Node(33))
        s_list.add_in_tail(Node(44))
        self.assertEqual(s_list.head.value, 11)
        self.assertEqual(s_list.tail.value, 44)

    def test_empty_fake_function(self):
        s_list = LinkedList2()
        s_list.add_in_head(Node(55))
        s_list.delete(55)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_empty_fake_function_2(self):
        s_list = LinkedList2()
        s_list.fake_function()
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)

    def test_delete_one_and_fake_function(self):
        s_list = LinkedList2()
        node_1 = Node(55)
        node_2 = Node(55)
        node_3 = Node(55)
        node_4 = Node(55)
        node_5 = Node(55)
        s_list.add_in_tail(node_1)
        s_list.add_in_tail(node_2)
        s_list.add_in_tail(node_3)
        s_list.add_in_tail(node_4)
        s_list.add_in_tail(node_5)
        s_list.delete(55)
        self.assertEqual(s_list.head, node_2)
        self.assertEqual(s_list.tail, node_5)

    def test_delete_all_and_fake_function(self):
        s_list = LinkedList2()
        node_1 = Node(55)
        node_2 = Node(55)
        node_3 = Node(55)
        node_4 = Node(55)
        node_5 = Node(55)
        s_list.add_in_tail(node_1)
        s_list.add_in_tail(node_2)
        s_list.add_in_tail(node_3)
        s_list.add_in_tail(node_4)
        s_list.add_in_tail(node_5)
        s_list.delete(55, True)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)


if __name__ == '__main__':
    unittest.main()
