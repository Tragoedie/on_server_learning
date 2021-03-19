import unittest
from on_server_learning.algorithms_1.stack_queue_deque.Stack import *


class Test_Stack(unittest.TestCase):

    def test_stack_size(self):
        stack = Stack()
        for i in range(1, 6):
            stack.push(i)
        self.assertEqual(stack.size(), 5)

    def test_stack_size_empty(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)

    def test_stack_pop(self):
        stack = Stack()
        for i in range(1, 6):
            stack.push(i)
        x = stack.pop()
        self.assertEqual(x, 5)
        self.assertEqual(stack.size(), 4)

    def test_stack_pop_empty(self):
        stack = Stack()
        for i in range(1, 6):
            stack.push(i)
        for i in range(5):
            stack.pop()
        self.assertEqual(stack.pop(), None)
        self.assertEqual(stack.size(), 0)

    def test_stack_push(self):
        stack = Stack()
        for i in range(1, 21):
            stack.push(i)
        x = stack.pop()
        self.assertEqual(stack.size(), 19)
        self.assertEqual(x, 20)

    def test_stack_peek(self):
        stack = Stack()
        for i in range(1, 21):
            stack.push(i)
        x = stack.peek()
        self.assertEqual(stack.size(), 20)
        self.assertEqual(x, 20)


if __name__ == '__main__':
    unittest.main()
