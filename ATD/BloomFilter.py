class BloomFilter:

    # конструктор:
    # постусловие: создан новый пустой фильтр Блюма с битовым массивом размера sz.
    def __init__(self, sz):
        pass

    # команды:
    # постусловие: в фильтр добавлено новая строка.
    def add(self, str1):
        pass

    # постусловие: фильтр очищен от всех элементов.
    def clear(self):
        pass

    # запросы:
    # проверка, имеется ли в фильтре значение value
    def is_value(self, str1):
        pass


from bitarray import bitarray


class BloomFilter:

    def __init__(self, sz):
        self.filter_len = sz
        self.bit_array = bitarray(sz)
        self.bit_array.setall(0)

    def hash1(self, str_1):
        # 17
        hash_str_1 = 0
        for c in str_1:
            hash_str_1 = hash_str_1 * 17 + ord(c)
        return hash_str_1 % self.filter_len

    def hash2(self, str1):
        # 223
        hash_str_2 = 0
        for c in str1:
            hash_str_2 = hash_str_2 * 223 + ord(c)
        return hash_str_2 % self.filter_len

    def add(self, str1):
        hash_1 = self.hash1(str1)
        hash_2 = self.hash2(str1)
        self.bit_array[hash_1] = 1
        self.bit_array[hash_2] = 1

    def clear(self):
        self.bit_array.setall(0)

    def is_value(self, str1):
        hash_1 = self.hash1(str1)
        hash_2 = self.hash2(str1)
        if self.bit_array[hash_1] == 1 and self.bit_array[hash_2] == 1:
            return True
        return False
