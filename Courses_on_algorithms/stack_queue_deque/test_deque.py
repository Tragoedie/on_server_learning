import unittest
from on_server_learning.algorithms_1.stack_queue_deque.deque_linked_list import *


class Test_Deque(unittest.TestCase):

    def test_addFront(self):
        deque = Deque()
        for i in range(1, 6):
            deque.addFront(i)
        deque.addFront(555)
        self.assertEqual(deque.size(), 6)
        self.assertEqual(deque.head.value, 555)

    def test_addFront_one(self):
        deque = Deque()
        deque.addFront(1)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.head.value, 1)
        self.assertEqual(deque.tail.value, 1)

    def test_addTail(self):
        deque = Deque()
        for i in range(1, 6):
            deque.addTail(i)
        deque.addTail(555)
        self.assertEqual(deque.size(), 6)
        self.assertEqual(deque.tail.value, 555)

    def test_addTail_one(self):
        deque = Deque()
        deque.addTail(1)
        self.assertEqual(deque.size(), 1)
        self.assertEqual(deque.head.value, 1)
        self.assertEqual(deque.tail.value, 1)

    def test_removeFront(self):
        deque = Deque()
        for i in range(1, 6):
            deque.addTail(i)
        x = deque.removeFront()
        self.assertEqual(x, 1)
        self.assertEqual(deque.size(), 4)

    def test_removeFront_one(self):
        deque = Deque()
        deque.addTail(1)
        x = deque.removeFront()
        self.assertEqual(x, 1)
        self.assertEqual(deque.size(), 0)
        self.assertIsNone(deque.head)
        self.assertIsNone(deque.tail)
        self.assertEqual(deque.removeFront(), None)

    def test_removeTail(self):
        deque = Deque()
        for i in range(1, 6):
            deque.addFront(i)
        x = deque.removeTail()
        self.assertEqual(x, 1)
        self.assertEqual(deque.size(), 4)

    def test_removeTail_one(self):
        deque = Deque()
        deque.addFront(1)
        x = deque.removeTail()
        self.assertEqual(x, 1)
        self.assertEqual(deque.size(), 0)
        self.assertIsNone(deque.head)
        self.assertIsNone(deque.tail)
        self.assertEqual(deque.removeTail(), None)


if __name__ == '__main__':
    unittest.main()
