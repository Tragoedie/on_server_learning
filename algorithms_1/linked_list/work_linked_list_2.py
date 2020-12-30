class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        massive = []
        while node is not None:
            if node.value == val:
                massive.append(node)
            node = node.next
        return massive

    def delete(self, val, all=False):
        node = self.head
        if node is None:
            return
        while node is not None:
            if node.value == val:
                if self.head == self.tail:
                    self.head = self.tail = None
                elif node.prev is None:
                    self.head = node.next
                    node.next.prev = None
                elif self.tail == node:
                    self.tail = node.prev
                    node.prev.next = None
                else:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                if all is False:
                    return
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.head = self.tail = newNode
        elif afterNode is None:
            self.tail.next = newNode
            self.tail = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode
            if afterNode == self.tail:
                self.tail = newNode
                return
            newNode.next.prev = newNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
