import unittest
from on_server_learning.algorithms_1.hashtable_bloom_powerset_nativecache.native_cashe import NativeCache


class Test_hash_table(unittest.TestCase):

    def test_put_empty_keys(self):
        table = NativeCache(5)
        table.put('aaa', 3)
        self.assertEqual(table.values[1], 3)
        self.assertEqual(table.slots[1], 'aaa')
        self.assertEqual(table.hits[1], 0)

    def test_put_not_empty_keys(self):
        table = NativeCache(5)
        table.put('aaa', 3)
        table.put('aaa', 5)
        self.assertEqual(table.values[1], 5)
        self.assertEqual(table.slots[1], 'aaa')
        self.assertEqual(table.hits[1], 0)

    def test_get_empty_keys(self):
        table = NativeCache(5)
        self.assertIsNone(table.get('aaa'))

    def test_get_not_empty_keys(self):
        table = NativeCache(5)
        table.put('aaa', 3)
        table.get('aaa')
        table.get('aaa')
        self.assertEqual(table.get('aaa'), 3)
        self.assertEqual(table.hits[1], 3)

    def test_is_key_empty_keys(self):
        table = NativeCache(5)
        self.assertFalse(table.is_key('aaa'))

    def test_is_key_not_empty_keys(self):
        table = NativeCache(5)
        table.put('aaa', 3)
        self.assertTrue(table.is_key('aaa'))
        self.assertEqual(table.hits[1], 1)

    def test_is_key_not_empty_keys_full(self):
        table = NativeCache(5)
        table.put('aaa', 1)
        table.put('bbb', 2)
        table.put('ccc', 3)
        table.put('ddd', 4)
        table.put('eee', 5)
        self.assertTrue(table.get('aaa'))
        self.assertTrue(table.get('bbb'))
        self.assertTrue(table.get('ccc'))
        self.assertTrue(table.get('ddd'))
        self.assertTrue(table.get('eee'))
        self.assertEqual(table.hits[0], 1)
        self.assertEqual(table.hits[1], 1)
        self.assertEqual(table.hits[2], 1)
        self.assertEqual(table.hits[3], 1)
        self.assertEqual(table.hits[4], 1)

    def test_put_full_cache(self):
        table = NativeCache(5)
        table.put('aaa', 1)
        table.put('bbb', 2)
        table.put('ccc', 3)
        table.put('ddd', 4)
        table.put('eee', 5)
        table.get('aaa')
        table.get('aaa')
        table.get('bbb')
        table.get('ccc')
        table.get('ddd')
        table.put('zzz', 6)
        self.assertTrue(table.get('aaa'))
        self.assertTrue(table.get('bbb'))
        self.assertTrue(table.get('ccc'))
        self.assertTrue(table.get('ddd'))
        self.assertTrue(table.get('zzz'))
        self.assertFalse(table.get('eee'))


if __name__ == '__main__':
    unittest.main()

