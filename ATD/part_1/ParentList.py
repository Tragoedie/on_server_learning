class ParentList:
    # конструктор
    # постусловие: создан новый пустой Linked List
    def __init__(self):
        pass

    # команды:
    # предусловие: список не пуст.
    # постусловие: курсор установлен на первый узел в списке.
    def head(self):
        pass

    # предусловие: список не пуст.
    # постусловие: курсор установлен на последний узел в списке.
    def tail(self):
        pass

    # предусловие: правее курсора есть элемент.
    # постусловие: курсор сдвинут на один узел вправо.
    def right(self):
        pass

    # предусловие: список не пуст.
    # постусловие: справа от текущего вставлен новый узел с заданным значением.
    def put_right(self, value):
        pass

    # предусловие: список не пуст.
    # постусловие: слева от текущего вставлен новый узел с заданным значением.
    def put_left(self, value):
        pass

    # предусловие: список не пуст.
    # постусловие: текущий узел удален.
    # курсор сместился к узлу справа, если он есть.
    # в противном случае курсор сместился к узлу слева, если он есть.
    def remove(self):
        pass

    # постусловие: список очищен от всех элементов.
    def clear(self):
        pass

    # постусловие: новый узел добавлен в хвост списка.
    def add_tail(self, value):
        pass

    # предусловие: список не пуст.
    # постусловие: значение текущего узла заменено на новое.
    def replace(self, value):
        pass

    # постусловие: курсор указывает на следующий узел с искомым значением, если такой узел найден.
    def find(self, value):
        pass

    # постусловие: из списка удалены все узлы с заданным значением.
    def remove_all(self, value):
        pass

    # запросы:
    # предусловие: курсор указывает на любой узел в списке.
    def get(self):  # получить значение текущего узла.
        pass

    def size(self):  # посчитать количество узлов в списке
        pass

    def is_head(self):  # находится ли курсор в начале списка?
        pass

    def is_tail(self):  # находится ли курсор в конце списка?
        pass

    def is_value(self):  # установлен ли курсор на какой - либо узел в списке (по сути, непустой ли список).
        pass

    # запросы статусов (возможные значения статусов)
    def get_head_status(self):  # успешно; список пуст
        pass

    def get_tail_status(self):  # успешно; список пуст
        pass

    def get_right_status(self):  # успешно; правее нету элемента
        pass

    def get_put_right_status(self):  # успешно; список пуст
        pass

    def get_put_left_status(self):  # успешно; список пуст
        pass

    def get_remove_status(self):  # успешно; список пуст
        pass

    def get_replace_status(self):  # успешно; список пуст
        pass

    def get_find_status(self):  # следующий найден;
        pass  # следующий не найден; список пуст

    def get_get_status(self):  # успешно; список пуст
        pass


# ATD LinkedList
class LinkedList(ParentList):
    def __init__(self):
        super().__init__()


# ATD TwoWayList
class TwoWayList(ParentList):
    def __init__(self):
        super().__init__()

    # команды
    # предусловие: курсор указывает не на первый узел в списке.
    # постусловие: курсор указывает на узел, который находится слева от текущего.
    def left(self):  # сдвинуть курсор на один узел вправо.
        pass

    # запросы статусов (возможные значения статусов)
    def get_left_status(self):  # успешно; левее нету элемента.
        pass


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class ParentList:
    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.head_status = ParentList.STATUS_ERR
        self.tail_status = ParentList.STATUS_ERR
        self.right_status = ParentList.STATUS_ERR
        self.put_right_status = ParentList.STATUS_ERR
        self.put_left_status = ParentList.STATUS_ERR
        self.remove_status = ParentList.STATUS_ERR
        self.replace_status = ParentList.STATUS_ERR
        self.find_status = ParentList.STATUS_ERR
        self.get_status = ParentList.STATUS_ERR

    def head(self):
        if self.head is not None:
            self.head_status = ParentList.STATUS_OK
            self.cursor = self.head
        else:
            self.head_status = ParentList.STATUS_ERR

    def tail(self):
        if self.tail is not None:
            self.tail_status = ParentList.STATUS_OK
            self.cursor = self.tail
        else:
            self.tail_status = ParentList.STATUS_ERR

    def right(self):
        if self.cursor.next is None or self.head is None:
            self.right_status = ParentList.STATUS_ERR
        else:
            self.right_status = ParentList.STATUS_OK
            self.cursor = self.cursor.next

    def put_right(self, value):
        if self.head is None:
            self.put_right_status = ParentList.STATUS_ERR
        else:
            node = Node(value)
            if self.is_tail():
                self.cursor.next = node
                node.prev = self.cursor
                self.tail = node
            else:
                node.next = self.cursor.next
                self.cursor.next.prev = node
                self.cursor.next = node
                node.prev = self.cursor
            self.put_right_status = ParentList.STATUS_OK

    def put_left(self, value):
        if self.head is None:
            self.put_left_status = ParentList.STATUS_ERR
        else:
            node = Node(value)
            if self.is_head():
                self.cursor.prev = node
                node.next = self.cursor
                self.head = node
            else:
                node.prev = self.cursor.prev
                self.cursor.prev.next = node
                node.next = self.cursor
                self.cursor.prev = node
            self.put_left_status = ParentList.STATUS_OK

    def remove(self):
        if self.head is None:
            self.remove_status = ParentList.STATUS_ERR
        else:
            if self.size() == 1:
                self.clean()
                return
        if self.cursor.prev is None:
            self.head = self.cursor.next
            self.cursor = self.head
        else:
            self.cursor.prev.next = self.cursor.next
        if self.cursor.next is None:
            self.tail = self.cursor.prev
        else:
            self.cursor.next.prev = self.cursor.prev
        self.remove_status = ParentList.STATUS_OK

    def remove_all(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                if self.size() == 1:
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
            node = node.next

    def clear(self):
        self.head = None
        self.tail = None
        self.cursor = None
        self.head_status = ParentList.STATUS_ERR
        self.tail_status = ParentList.STATUS_ERR
        self.right_status = ParentList.STATUS_ERR
        self.put_right_status = ParentList.STATUS_ERR
        self.put_left_status = ParentList.STATUS_ERR
        self.remove_status = ParentList.STATUS_ERR
        self.replace_status = ParentList.STATUS_ERR
        self.find_status = ParentList.STATUS_ERR
        self.get_status = ParentList.STATUS_ERR

    def add_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def replace(self, value):
        if self.list_head is None:
            self.replace_status = ParentList.STATUS_ERR
        else:
            self.cursor.value = value
            self.replace_status = ParentList.STATUS_OK

    def find(self, value):
        if self.cursor is None:
            node = self.head
        else:
            node = self.cursor
        while node is not None:
            if node.value == value:
                self.cursor = node
                self.find_status = ParentList.STATUS_OK
                return
            node = node.next
        self.find_status = ParentList.STATUS_ERR

    def get(self):
        if self.cursor is None or self.head is None:
            self.get_status = ParentList.STATUS_ERR
        else:
            self.get_status = ParentList.STATUS_OK
            return self.cursor.value

    def is_head(self):
        return self.head == self.cursor

    def is_tail(self):
        return self.tail == self.cursor

    def is_value(self):
        return self.cursor is not None

    def size(self):
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length

    def get_head_status(self):
        return self.head_status

    def get_tail_status(self):
        return self.tail_status

    def get_right_status(self):
        return self.right_status

    def get_put_right_status(self):
        return self.put_right_status

    def get_put_left_status(self):
        return self.put_left_status

    def get_remove_status(self):
        return self.remove_status

    def get_replace_status(self):
        return self.replace_status

    def get_find_status(self):
        return self.find_status

    def get_get_status(self):
        return self.get_status


class LinkedList(ParentList):
    pass


class TwoWayList(ParentList):
    def __init__(self):
        super.__init__()
        self.left_status = ParentList.STATUS_ERR

    def left(self):
        if self.cursor.prev is None or self.head is None:
            self.left_status = self.STATUS_ERR
        else:
            self.left_status = self.STATUS_OK
            self.cursor = self.cursor.prev

    def get_left_status(self):
        return self.left_status

