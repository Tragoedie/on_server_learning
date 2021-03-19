from bitarray import bitarray


class BloomFilter:

    def __init__(self, f_len):  # создаём битовый массив длиной f_len
        self.filter_len = f_len
        self.bit_array = bitarray(f_len)
        self.bit_array.setall(0)

    def hash1(self, str1):
        # 17
        hash_str_1 = 0
        for c in str1:
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

    def is_value(self, str1):
        hash_1 = self.hash1(str1)
        hash_2 = self.hash2(str1)
        if self.bit_array[hash_1] == 1 and self.bit_array[hash_2] == 1:
            return True
        return False

    def print_all(self):
        for i in range(self.filter_len):
            print(self.bit_array[i])

