import unittest
from on_server_learning.algorithms_1.hashtable_bloom_powerset_nativecache.hash_table import HashTable


class Test_hash_table(unittest.TestCase):

    def test_hash_fun(self):   
        table = HashTable(5, 2)
        sum_1 = table.hash_fun('aaa')
        sum_2 = 0
        for i in range(3):
            sum_2 += 97 % 5
        sum_2 %= 5
        self.assertEqual(sum_1, sum_2)

    def test_hash_fun_2(self):
        table = HashTable(5, 2)
        sum_1 = table.hash_fun('Hello!')
        sum_2 = (72 % 5 + 101 % 5 + 108 % 5 + 108 % 5 + 111 % 5 + 33 % 5) % 5
        self.assertEqual(sum_1, sum_2)

    def test_seek_slot_1(self):
        table = HashTable(5, 2)
        sum_1 = table.hash_fun('aaa')
        sum_2 = table.seek_slot('aaa')
        self.assertEqual(sum_1, sum_2)
        self.assertEqual(sum_2, 1)

    def test_seek_slot_2(self):
        table = HashTable(5, 2)
        for i in range(5):
            table.put('aaa')
        slot = table.seek_slot('aaa')
        self.assertIsNone(slot)

    def test_seek_put_1(self):
        table = HashTable(5, 2)
        for i in range(5):
            table.put('aaa')
        slot = table.put('aaa')
        self.assertIsNone(slot)

    def test_seek_put_2(self):
        table = HashTable(5, 2)
        sum_1 = table.hash_fun('aaa')
        sum_2 = table.put('aaa')
        self.assertEqual(sum_1, sum_2)

    def test_seek_find_1(self):
        table = HashTable(5, 2)
        table.put('aaa')
        table.put('bbb')
        table.put('ccc')
        table.put('ddd')
        table.put('eee')
        slot_1 = table.find('aaa')
        slot_2 = table.find('bbb')
        slot_3 = table.find('ccc')
        slot_4 = table.find('ddd')
        slot_5 = table.find('eee')
        self.assertEqual(slot_1, 1)
        self.assertEqual(slot_2, 4)
        self.assertEqual(slot_3, 2)
        self.assertEqual(slot_4, 0)
        self.assertEqual(slot_5, 3)

    def test_seek_find_2(self):
        table = HashTable(5, 2)
        table.put('aaa')
        table.put('bbb')
        table.put('ccc')
        table.put('ddd')
        table.put('eee')
        slot = table.find('xxx')
        self.assertIsNone(slot)


if __name__ == '__main__':
    unittest.main()
