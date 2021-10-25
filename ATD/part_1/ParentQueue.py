class ParentQueue:
    # конструктор:
    # постусловие: создана новая пустая очередь.
    def __init__(self):
        pass

    # команды:
    # постусловие: элемент добавлен в конец очереди.
    def addTail(self, item):
        pass

    # предусловие: очередь не пустая
    # постусловие: элемент удален из начала очереди, получено значение удаленного элемента.
    def removeFront(self):
        pass

    # постусловие: очередь очищена от всех элементов.
    def clear(self):
        pass

    # запросы:
    def size(self):  # посчитать количество узлов в списке.
        pass

    # предусловие: очередь не пустая.
    def get(self):  # получить значение элемента в начале очереди без удаления.
        pass

    # запросы статусов (возможные значения статусов).
    def get_remove_front_status(self):  # успешно; очередь пуста
        pass

    def get_get_status(self):
        pass


# ATD Queue
class Queue(ParentQueue):
    pass


# ATD Deque
class Deque(ParentQueue):
    pass

    # команды
    # постусловие: элемент добавлен в начало очереди.
    def addFront(self, item):
        pass

    # постусловие: элемент удален с конца очереди, получено значение удаленного элемента.
    def removeTail(self):
        pass

    # запросы статусов (возможные значения статусов)
    def get_remove_tail_status(self):  # успешно; очередь пуста
        pass


class ParentQueue:
    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self):
        self.parent_queue = []
        self.remove_front = ParentQueue.STATUS_ERR
        self.get_status = ParentQueue.STATUS_ERR

    def addTail(self, item):
        self.parent_queue.append(item)

    def removeFront(self):
        if self.parent_queue is not []:
            self.remove_front = ParentQueue.STATUS_OK
            return self.parent_queue.pop(0)
        self.remove_front = ParentQueue.STATUS_ERR
        return None

    def clear(self):
        self.parent_queue = []
        self.remove_front = ParentQueue.STATUS_ERR
        self.get_status = ParentQueue.STATUS_ERR

    def size(self):
        return len(self.parent_queue)

    def get(self):
        if self.parent_queue is not []:
            self.get_status = ParentQueue.STATUS_OK
            return self.parent_queue[0]
        else:
            self.get_status = ParentQueue.STATUS_ERR

    def get_remove_front_status(self):
        return self.remove_front

    def get_get_status(self):
        return self.get_status


class Queue(ParentQueue):
    def __init__(self):
        super().__init__()


class Deque(ParentQueue):
    def __init__(self):
        super().__init__()
        self.remove_tail_status = ParentQueue.STATUS_ERR

    def addFront(self, item):
        self.parent_queue.insert(0, item)

    def removeTail(self):
        if self.parent_queue:
            self.remove_tail_status = ParentQueue.STATUS_OK
            return self.parent_queue.pop()
        self.remove_tail_status = ParentQueue.STATUS_ERR
        return None

    def clear(self):
        self.parent_queue = []
        self.remove_front = ParentQueue.STATUS_ERR
        self.remove_tail_status = ParentQueue.STATUS_ERR
        self.get_status = ParentQueue.STATUS_ERR

    def get_remove_tail_status(self):
        return self.remove_tail_status
