class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

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
        last_node = None
        if node is None:
            return
        while node is not None:
            if node.value == val:
                if last_node is None:
                    self.head = node.next
                else:
                    last_node.next = node.next
                if self.tail == node:
                    self.tail = last_node
                if all is False:
                    return
            else:
                last_node = node
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
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if newNode.next is None:
                self.tail = newNode
                return
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            if afterNode == self.tail:
                self.tail = newNode



