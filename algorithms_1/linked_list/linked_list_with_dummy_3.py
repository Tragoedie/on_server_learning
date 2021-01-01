class Node:
    def __init__(self, v, fake=False):
        self.value = v
        self.prev = None
        self.next = None
        self.fake = fake


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head_fake = Node(None, True)
        self.tail_fake = Node(None, True)
        self.head_fake.next = self.tail_fake
        self.tail_fake.prev = self.head_fake

    def clean(self):
        self.head = None
        self.tail = None
        self.head_fake.next = self.tail_fake
        self.tail_fake.prev = self.head_fake

    def fake_function(self):
        if self.head_fake.next == self.tail_fake:
            self.clean
        else:
            self.head = self.head_fake.next
            self.tail = self.tail_fake.prev

    def add_in_tail(self, item):
        item.prev = self.tail_fake.prev
        self.tail_fake.prev.next = item
        self.tail_fake.prev = item
        item.next = self.tail_fake
        self.fake_function()

    def find(self, val):
        node = self.head_fake.next
        while node.fake is False:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head_fake.next
        massive = []
        while node.fake is False:
            if node.value == val:
                massive.append(node)
            node = node.next
        return massive

    def delete(self, val, all=False):
        node = self.head_fake.next
        while node.fake is False:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if all is False:
                    self.fake_function()
                    return
            node = node.next
        self.fake_function()

    def len(self):
        length = 0
        node = self.head_fake.next
        while node.fake is False:
            node = node.next
            length += 1
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode
            newNode.prev = afterNode
            newNode.next.prev = newNode
            self.fake_function()

    def add_in_head(self, newNode):
        newNode.next = self.head_fake.next
        self.head_fake.next.prev = newNode
        self.head_fake.next = newNode
        newNode.prev = self.head_fake
        self.fake_function()

    def print_all_nodes(self):
        node = self.head_fake.next
        while node.fake is False:
            print(node.value)
            node = node.next



