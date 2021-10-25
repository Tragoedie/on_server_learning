class Queue:
    # конструктор:
    # постусловие: создана новая пустая очередь.
    def __init__(self):
        pass

    # команды:
    # постусловие: элемент добавлен в конец очереди.
    def enqueue(self, item):
        pass

    # предусловие: очередь не пустая
    # постусловие: элемент удален из начала очереди, получено значение удаленного элемента.
    def dequeue(self):
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
    def get_enqueue_status(self):
        pass

    def get_dequeue_status(self):
        pass

    def get_get_status(self):
        pass


class Queue:
    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self):
        self.queue = []
        self.enqueue_status = Queue.STATUS_ERR
        self.dequeue_status = Queue.STATUS_ERR
        self.get_status = Queue.STATUS_ERR

    def enqueue(self, item):
        self.queue.append(item)
        self.enqueue_status = Queue.STATUS_OK

    def dequeue(self):
        if self.queue is not []:
            self.dequeue_status = Queue.STATUS_OK
            return self.queue.pop(0)
        else:
            self.dequeue_status = Queue.STATUS_ERR
            return None

    def clear(self):
        self.queue = []
        self.enqueue_status = Queue.STATUS_ERR
        self.dequeue_status = Queue.STATUS_ERR
        self.get_status = Queue.STATUS_ERR

    def size(self):
        return len(self.queue)

    def get(self):
        if self.queue is not []:
            self.get_status = Queue.STATUS_OK
            return self.queue[0]
        else:
            self.get_status = Queue.STATUS_ERR

    def get_enqueue_status(self):
        return self.enqueue_status

    def get_dequeue_status(self):
        return self.dequeue_status

    def get_get_status(self):
        return self.get_status

