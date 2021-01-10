from on_server_learning.algorithms_1.stack_queue_deque.Stack import Stack


class Queue:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, item):
        self.stack_1.push(item)

    def dequeue(self):
        if self.stack_2.size() == 0:
            while self.stack_1.size() != 0:
                number = self.stack_1.pop()
                self.stack_2.push(number)
        return self.stack_2.pop()

    def size(self):
        sum_of_len = self.stack_1.size() + self.stack_2.size()
        return sum_of_len


qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.enqueue(8)
print(qu.size())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())
print(qu.dequeue())