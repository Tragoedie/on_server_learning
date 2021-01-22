import unittest
from on_server_learning.algorithms_1.hash_table.native_dictionary import NativeDictionary


class Test_hash_table(unittest.TestCase):

    def test_put_empty_keys(self):
        table = NativeDictionary(5)
        table.put('aaa', 3)
        self.assertEqual(table.values[1], 3)
        self.assertEqual(table.slots[1], 'aaa')

    def test_put_not_empty_keys(self):
        table = NativeDictionary(5)
        table.put('aaa', 3)
        table.put('aaa', 5)
        self.assertEqual(table.values[1], 5)
        self.assertEqual(table.slots[1], 'aaa')

    def test_get_empty_keys(self):
        table = NativeDictionary(5)
        self.assertIsNone(table.get('aaa'))

    def test_get_not_empty_keys(self):
        table = NativeDictionary(5)
        table.put('aaa', 3)
        self.assertEqual(table.get('aaa'), 3)

    def test_get_not_empty_keys_full(self):
        table = NativeDictionary(5)
        table.put('aaa', 1)
        table.put('bbb', 2)
        table.put('ccc', 3)
        table.put('ddd', 4)
        table.put('eee', 5)
        table.put('zzz', 6)
        self.assertEqual(table.get('aaa'), 1)
        self.assertEqual(table.get('bbb'), 2)
        self.assertEqual(table.get('ccc'), 3)
        self.assertEqual(table.get('ddd'), 4)
        self.assertEqual(table.get('eee'), 5)
        self.assertIsNone(table.get('zzz'))

    def test_is_key_empty_keys(self):
        table = NativeDictionary(5)
        self.assertFalse(table.is_key('aaa'))

    def test_is_key_not_empty_keys(self):
        table = NativeDictionary(5)
        table.put('aaa', 3)
        self.assertTrue(table.is_key('aaa'))

    def test_is_key_not_empty_keys_full(self):
        table = NativeDictionary(5)
        table.put('aaa', 1)
        table.put('bbb', 2)
        table.put('ccc', 3)
        table.put('ddd', 4)
        table.put('eee', 5)
        table.put('zzz', 6)
        self.assertTrue(table.get('aaa'))
        self.assertTrue(table.get('bbb'))
        self.assertTrue(table.get('ccc'))
        self.assertTrue(table.get('ddd'))
        self.assertTrue(table.get('eee'))
        self.assertFalse(table.get('zzz'))


if __name__ == '__main__':
    unittest.main()
