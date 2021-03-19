class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_node(self, value):
        return Node(value)

    def node_prev_tail(self):
        node = self.head
        while node.next != self.tail:
            node = node.next
        return node

    def clean(self):
        self.head = None
        self.tail = None

    def addFront(self, item):
        node = self.create_node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addTail(self, item):
        node = self.create_node(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def removeFront(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            node = self.head
            self.clean()
            return node.value
        node = self.head
        self.head = self.head.next
        return node.value

    def removeTail(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            node = self.head
            self.clean()
            return node.value
        node = self.node_prev_tail()
        node_tail = self.tail
        self.tail = node
        self.tail.next = None
        return node_tail.value

    def size(self):
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
