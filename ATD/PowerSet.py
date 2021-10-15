from on_server_learning.ATD.HashTable import HashTable


# ATD PowerSet
class PowerSet(HashTable):
    # конструктор:
    # постусловие: создан новое множество размера sz.
    def __init__(self, sz):
        pass

    # команды:
    # предусловие: в таблице имеется свободный слот, в множестве отсутсвует такой же элемент.
    # постусловие: в таблицу добавлен новый элемент.
    def put(self, value):
        pass

    # запросы:
    # количество элементов в таблице
    def size(self):
        pass

    # создано новое множество, содержащее в себе пересечение множеств.
    def intersection(self, set2):
        pass

    # создано новое множество, содержащее в себе объединение множеств.
    def union(self, set2):
        pass

    # создано новое множество, содержащее в себе разность множеств.
    def difference(self, set2):  # разница
        pass

    # дополнительные запросы:
    def issubset(self, set2):  # является ли второе множество подмножеством первого
        pass


class PowerSet(HashTable):
    # конструктор:
    # постусловие: создан новое множество размера sz.
    def __init__(self, sz):
        super().__init__()
        self.size = sz

    def put(self, value):
        empty_slot = self.seek_slot(value)
        if empty_slot is not None and self.get(value) is None:
            self.slots[empty_slot] = value
            self.put_status = HashTable.STATUS_OK
        self.put_status = HashTable.STATUS_ERR

    def size(self):
        return self.size

    def intersection(self, set2):
        intersection_set = PowerSet()
        for item in self.slots:
            if set2.get(item) is not None:
                intersection_set.put(item)
        return intersection_set

    def union(self, set2):
        intersection_set = PowerSet()
        for i in set2.slots:
            intersection_set.put(i)
        for j in self.slots:
            intersection_set.put(j)
        return intersection_set

    def difference(self, set2):
        intersection_set = PowerSet()
        for item in self.slots:
            if set2.get(item) is None:
                intersection_set.put(item)
        return intersection_set

    def issubset(self, set2):
        for item in set2.slots:
            if self.get(item) is None:
                return False
        return True
