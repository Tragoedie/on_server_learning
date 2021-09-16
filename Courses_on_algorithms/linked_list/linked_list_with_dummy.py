from on_server_learning.Courses_on_algorithms.linked_list.work_linked_list_2 import Node
from on_server_learning.Courses_on_algorithms.linked_list.work_linked_list_2 import LinkedList2


class Node_with_fake(Node):
    def __init__(self, v, fake=False):
        super().__init__(v)
        self.fake = fake


class LinkedList2_with_dummy(LinkedList2):
    def __init__(self):
        super().__init__()
        self.head_fake = Node_with_fake(None, True)
        self.tail_fake = Node_with_fake(None, True)

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = self.head_fake
            self.head_fake.next = item
        else:
            self.tail.next = item
            item.prev = self.tail
        item.next = self.tail_fake
        self.tail_fake.prev = item
        self.tail = item

    def deleted(self, val, all=False):
        node = self.head
        while node is not None and node.fake is False:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if all is False:
                    break
            node = node.next
        if self.head_fake.next == self.tail_fake:
            self.head = None
            self.tail = None
        else:
            self.head = self.head_fake.next
            self.tail = self.tail_fake.prev
