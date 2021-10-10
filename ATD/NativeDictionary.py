class NativeDictionary:
    # конструктор:
    # постусловие: создан новый пустой ассоциативный массив размера sz.
    def __init__(self, sz):
        pass

    # команды:
    # предусловие: в таблице имеется свободный слот.
    # постусловие: в таблицу добавлена пара ключ-значение.
    def put(self, key, value):
        pass

    # предусловие: в таблице имеется ключ.
    # постусловие: в таблице удалена пара ключ-значение.
    def remove(self, key, value):
        pass

    # запросы:
    # предусловие: ключ содержится в таблице.
    # постусловие: возвращает индекс слота с ключом или None
    def get(self, value):
        pass

    # проверка, имеется ли в слотах такой ключ
    def is_key(self, key):
        pass

    # количество элементов в таблице
    def size(self):
        pass

    # запросы статусов (возможные значения статусов).
    def get_put_status(self):  # успешно; Hash таблица переполнена.
        pass

    def get_remove_status(self):  # успешно; значение не найдено.
        pass


class NativeDictionary:

    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.put_status = NativeDictionary.STATUS_ERR
        self.remove_status = NativeDictionary.STATUS_ERR

    def hash_fun(self, key):
        hash = 0
        for pos in key:
            hash += ord(pos) % self.size
        return hash % self.size

    def next_index(self, hash_old):
        return (hash_old + 2) % self.size

    def put(self, key, value):
        slot = self.hash_fun(key)
        index = slot
        while self.slots[index] is not None and self.slots[index] != key:
            index = self.next_index(index)
            if index == slot:
                self.put_status = NativeDictionary.STATUS_ERR
                return None
        self.put_status = NativeDictionary.STATUS_OK
        self.slots[index] = key
        self.values[index] = value

    def remove(self, key):
        index_slot = self.get(key)
        if index_slot is not None:
            self.slots[index_slot] = None
            self.values[index_slot] = [None]
            self.remove_status = NativeDictionary.STATUS_OK
        else:
            self.remove_status = NativeDictionary.STATUS_ERR

    def get(self, key):
        slot = self.hash_fun(key)
        index = slot
        while self.slots[index] is not None:
            if self.slots[index] == key:
                return index
            index = self.next_index(index)
            if index == slot:
                break
        return None

    def is_key(self, key):
        if self.get(key) is not None:
            return True
        return False

    def size(self):
        return self.size

    def get_put_status(self):
        return self.put_status

    def get_remove_status(self):
        return self.remove_status
