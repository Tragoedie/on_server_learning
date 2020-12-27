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

    def delete(self, val, all):
        node = self.head
        if node is None:
            return
        else:
            if node.value == val:
                self.head = node.next
                node = self.head
                if all is False:
                    return
                else:
                    self.delete(val, all)
            else:
                while node is not None:
                    if node.value == val:
                        last_node.next = node.next
                        node = last_node.next
                        if all is False:
                            return
                    else:
                        last_node = node
                        node = node.next
                self.tail = last_node

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        if self.head is not None:
            node = self.head
            length = 1
            while node.next is not None:
                node = node.next
                length += 1
        return length

    def insert(self, afterNode, newNode):
        if self.head is None:
            self.tail = self.head = newNode
            return
        if afterNode is None:
            return
        newNode.next = afterNode.next
        afterNode.next = newNode
        if afterNode == self.tail:
            self.tail = newNode



