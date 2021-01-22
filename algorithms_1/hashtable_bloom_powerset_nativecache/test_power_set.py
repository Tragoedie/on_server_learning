import unittest
from on_server_learning.algorithms_1.hashtable_bloom_powerset_nativecache.power_set import PowerSet
from datetime import datetime


class Test_power_set(unittest.TestCase):

    def test_put_empty(self):
        set1 = PowerSet()
        set1.put(123)
        self.assertTrue(set1.get(123))

    def test_put_not_empty(self):
        set1 = PowerSet()
        for i in range(10):
            set1.put(i)
        set1.put('Hello')
        set1.put('Hello')
        self.assertFalse(set1.get(123))
        self.assertEqual(set1.size(), 11)

    def test_remove(self):
        set1 = PowerSet()
        for i in range(10):
            set1.put(i)
        self.assertTrue(set1.remove(1))
        self.assertFalse(set1.remove('1'))
        self.assertEqual(set1.size(), 9)

    def test_intersection_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(20):
            if i % 2 == 0:
                set1.put(i)
            else:
                set2.put(i)
        set3 = set1.intersection(set2)
        self.assertEqual(set3.size(), 0)

    def test_intersection_not_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(10):
            set1.put(i)
        for j in range(5):
            set2.put(j)
        set3 = set1.intersection(set2)
        self.assertEqual(set3.size(), 5)
        self.assertTrue(set3.get(0))
        self.assertTrue(set3.get(1))
        self.assertTrue(set3.get(2))
        self.assertTrue(set3.get(3))
        self.assertTrue(set3.get(4))

    def test_union_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(20):
            set1.put(i)
        set3 = set1.union(set2)
        self.assertEqual(set3.size(), set1.size())
        self.assertEqual(set3.get(3), set1.get(3))

    def test_union_not_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(20):
            if i % 2 == 0:
                set1.put(i)
            else:
                set2.put(i)
        set3 = set1.union(set2)
        self.assertEqual(set3.size(), 20)
        self.assertEqual(set3.get(0), set1.get(0))
        self.assertEqual(set3.get(1), set2.get(1))
        self.assertEqual(set3.get(2), set1.get(2))
        self.assertEqual(set3.get(3), set2.get(3))

    def test_difference_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(10):
            set1.put(i)
        for j in range(10):
            set2.put(j)
        set3 = set1.difference(set2)
        self.assertEqual(set3.size(), 0)

    def test_difference_not_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(15):
            set1.put(i)
        for j in range(10):
            set2.put(j)
        set3 = set1.difference(set2)
        self.assertEqual(set3.size(), 5)
        self.assertTrue(set3.get(10))
        self.assertTrue(set3.get(11))
        self.assertTrue(set3.get(12))
        self.assertTrue(set3.get(13))
        self.assertTrue(set3.get(14))

    def test_issubset_all(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(10):
            set1.put(i)
        for j in range(5):
            set2.put(j)
        self.assertTrue(set1.issubset(set2))

    def test_issubset_all_swap(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(5):
            set1.put(i)
        for j in range(10):
            set2.put(j)
        self.assertFalse(set1.issubset(set2))

    def test_issubset_false(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(10):
            set1.put(i)
        for j in range(5, 15):
            set2.put(j)
        self.assertFalse(set1.issubset(set2))

    def test_speed(self):
        set1 = PowerSet()
        current_datetime = datetime.now()
        print(current_datetime)
        for i in range(50000):
            set1.put(i)
        current_datetime = datetime.now()
        print(current_datetime)
        set1.put(100000)
        current_datetime = datetime.now()
        print(current_datetime)
        self.assertTrue(set1.get(25000))
        current_datetime = datetime.now()
        print(current_datetime)
        self.assertTrue(set1.remove(25000))
        current_datetime = datetime.now()
        print(current_datetime)


if __name__ == '__main__':
    unittest.main()
