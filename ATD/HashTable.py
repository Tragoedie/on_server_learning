class HashTable:
    # конструктор:
    # постусловие: создана новая пустая Hash таблица определенного размера.
    def __init__(self, max_size):
        pass

    # команды:
    # предусловие: таблица не заполнена.
    # постусловие: новый элемент добавлен.
    def put(self, value):
        pass

    # предусловие: значение есть в списке.
    # постусловие: значение удалено.
    def remove(self, value):
        pass

    # запросы:
    # предусловие: поиск значения, возвращает слот или None.
    def find(self, value):
        pass

    # запросы статусов (возможные значения статусов).
    def get_put_status(self):  # успешно; Hash таблица переполнена.
        pass

    def get_remove_status(self):  # успешно; значение не найдено.
        pass

    def get_find_status(self):  # успешно; значение не найдено.
        pass


class HashTable:

    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self, max_size):
        self.size = max_size
        self.step = 2
        self.slots = [None] * self.size
        self.put_status = HashTable.STATUS_ERR
        self.remove_status = HashTable.STATUS_ERR
        self.find_status = HashTable.STATUS_ERR

    def hash_fun(self, value):
        hash = 0
        for pos in value:
            hash += ord(pos) % self.size
        return hash % self.size

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        slot_seek = slot
        while self.slots[slot_seek] is not None:
            slot_seek = self.next_index(slot_seek)
            if slot_seek == slot:
                return None
        return slot_seek

    def next_index(self, hash_old):
        return (hash_old + self.step) % self.size

    def put(self, value):
        empty_slot = self.seek_slot(value)
        if empty_slot is not None:
            self.slots[empty_slot] = value
            self.put_status = HashTable.STATUS_OK
            return empty_slot
        self.put_status = HashTable.STATUS_ERR
        return None

    def remove(self, value):
        index_slot = self.get(value)
        if index_slot is not None:
            self.slots[index_slot] = None
            self.remove_status = HashTable.STATUS_OK
        else:
            self.remove_status = HashTable.STATUS_ERR

    def get(self, value):
        slot = self.hash_fun(value)
        slot_seek = slot
        while self.slots[slot_seek] is not None:
            if self.slots[slot_seek] == value:
                self.find_status = HashTable.STATUS_OK
                return slot_seek
            slot_seek = self.next_index(slot_seek)
            if slot_seek == slot:
                self.find_status = HashTable.STATUS_ERR
                break
        return None

    def get_put_status(self):
        return self.put_status

    def get_remove_status(self):
        return self.remove_status

    def get_get_status(self):
        return self.find_status
