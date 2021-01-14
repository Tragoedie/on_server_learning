class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1

    def add(self, value):
        item = Node(value)
        if self.head is None:
            self.head = self.tail = item
            item.next = None
            item.prev = None
            return
        node = self.head
        while node is not None:
            if self.compare(item.value, node.value) < 1 and self.__ascending is True or \
                    self.compare(item.value, node.value) > -1 and self.__ascending is False:
                if node is self.head:
                    node.prev = item
                    item.next = node
                    self.head = item
                    return
                item.prev = node.prev
                node.prev.next = item
                node.prev = item
                item.next = node
                return
            node = node.next
        self.tail.next = item
        item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if self.__ascending is True and node.value > val or self.__ascending is False and node.value < val:
                return None
            if node.value == val:
                return node
            node = node.next
        return None

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

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1

