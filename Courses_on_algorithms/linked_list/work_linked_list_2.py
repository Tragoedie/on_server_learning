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
        while node is not None:
            if node.value == val:
                if self.len() == 1:
                    self.clean()
                    return
                if node.prev is None:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                if node.next is None:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
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
            newNode.next = None
            newNode.prev = None
        elif afterNode is None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            newNode.next = None
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
            newNode.next = None
            newNode.prev = None
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
