# АТД DynArray
class AbstractDynArray:

    # конструктор:
    # постусловие: создан пустой динамический массив, определенного размера.
    def __init__(self):
        pass

    # команды:
    # постусловие: элемент добавлен в конец массива.
    def append(self, item):
        pass

    # предусловие: корректный индекс, в пределах границ массива.
    # постусловие: новый элемент вставлен по индексу, остальные элементы смещены вправо,
    #              если индекс равен длинне массива, то элемент вставлен в конец списка.
    def insert(self, index, item):
        pass

    # предусловие: корректный индекс, в пределах границ массива.
    # постусловие: значение элемента по заданному индексу заменено на новое.
    def replace(self, index, value):
        pass

    # предусловие: корректный индекс, в пределах границ массива.
    # постусловие: удален элемент по индексу, остальные элементы сдвинуты влево.
    def delete(self, item):
        pass

    # постусловие: список очищен от всех элементов.
    def clear(self):
        pass

    # запросы:
    # предусловие: корректный индекс (в пределах границ массива)
    def get(self, index):  # получить элемент по индексу
        pass

    def size(self):  # посчитать длинну массива
        pass

    # запросы статусов (возможные значения статусов).
    def get_append_status(self):  # успешно; массив переполнен.
        pass

    def get_insert_status(self):  # успешно; индекс не корректен.
        pass

    def get_replace_status(self):  # успешно; индекс не корректен.
        pass

    def get_delete_status(self):  # успешно; индекс не корректен.
        pass

    def get_get_status(self):  # успешно; индекс не корректен.
        pass


import ctypes


class DynArray:
    STATUS_OK = 1
    STATUS_ERR = 2

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.__make_array__(self.capacity)
        self.append_status = DynArray.STATUS_ERR
        self.insert_status = DynArray.STATUS_ERR
        self.replace_status = DynArray.STATUS_ERR
        self.delete_status = DynArray.STATUS_ERR
        self.get_status = DynArray.STATUS_ERR

    def __make_array__(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __resize__(self, new_capacity):
        new_array = self.__make_array__(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.count == self.capacity:
            self.append_status = DynArray.STATUS_ERR
            self.__resize__(2 * self.capacity)
        self.array[self.count] = item
        self.count += 1
        self.append_status = DynArray.STATUS_OK

    def insert(self, index, item):
        if index < 0 or index > self.count:
            self.insert_status = DynArray.STATUS_ERR
            raise IndexError('Index is out of bounds')
        if self.count == self.capacity:
            self.__resize__(2 * self.capacity)
        if index == self.count:
            self.append(item)
        else:
            for i in range(self.count, index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = item
            self.count += 1
        self.insert_status = DynArray.STATUS_OK

    def replace(self, index, value):
        if index < 0 or index > self.count:
            self.replace_status = DynArray.STATUS_ERR
            raise IndexError('Index is out of bounds')
        else:
            self.array[index] = value
            self.replace_status = DynArray.STATUS_OK

    def delete(self, index):
        if index < 0 or index >= self.count:
            self.delete_status = DynArray.STATUS_ERR
            raise IndexError('Index is out of bounds')
        else:
            for i in range(index, self.count - 1):
                self.array[i] = self.array[i + 1]
            self.count -= 1
        if self.count < (0.5 * self.capacity):
            if self.capacity == 16:
                return
            new_capacity = int(self.capacity / 1.5)
            if new_capacity > 16:
                self.__resize__(new_capacity)
            elif new_capacity < 16:
                new_capacity = 16
                self.__resize__(new_capacity)
        self.delete_status = DynArray.STATUS_OK

    def clear(self):
        self.count = 0
        self.capacity = 16
        self.array = self.__make_array__(self.capacity)
        self.append_status = DynArray.STATUS_ERR
        self.insert_status = DynArray.STATUS_ERR
        self.replace_status = DynArray.STATUS_ERR
        self.delete_status = DynArray.STATUS_ERR
        self.get_status = DynArray.STATUS_ERR

    def get(self, index):
        if index < 0 or index >= self.count:
            self.get_status = DynArray.STATUS_ERR
            raise IndexError('Index is out of bounds')
        self.get_status = DynArray.STATUS_OK
        return self.array[index]

    def size(self):
        return self.count

    def get_append_status(self):
        return self.append_status

    def get_insert_status(self):
        return self.insert_status

    def get_replace_status(self):
        return self.replace_status

    def get_delete_status(self):
        return self.delete_status

    def get_get_status(self):
        return self.get_status
