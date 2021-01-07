class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def create_node(self, value):
        return Node(value)

    def enqueue(self, value):
        item = self.create_node(value)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def dequeue(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        return node.value

    def size(self):
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length
