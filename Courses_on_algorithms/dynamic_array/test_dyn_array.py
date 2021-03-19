import unittest
from on_server_learning.algorithms_1.dynamic_array.DynArray import *


class Test_dyn_array(unittest.TestCase):

    def test_insert_buffer_not_exceeded(self):
        dyn_array = DynArray()
        for i in range(10):
            dyn_array.append(i)
        dyn_array.insert(8, 555)
        self.assertEqual(dyn_array[8], 555)
        self.assertEqual(dyn_array.capacity, 16)

    def test_insert_buffer_not_exceeded_2(self):
        dyn_array = DynArray()
        for i in range(45):
            dyn_array.append(i)
        dyn_array.insert(16, 555)
        self.assertEqual(dyn_array[16], 555)
        self.assertEqual(dyn_array.capacity, 64)

    def test_insert_buffer_exceeded(self):
        dyn_array = DynArray()
        for i in range(16):
            dyn_array.append(i)
        dyn_array.insert(16, 555)
        self.assertEqual(dyn_array[16], 555)
        self.assertEqual(dyn_array.capacity, 32)

    def test_insert_index_error(self):
        dyn_array = DynArray()
        for i in range(16):
            dyn_array.append(i)
        with self.assertRaises(IndexError) as context:
            dyn_array.insert(32, 555)
        self.assertTrue('Index is out of bounds' in str(context.exception))

    def test_delete_buffer_not_exceeded(self):
        dyn_array = DynArray()
        for i in range(10):
            dyn_array.append(i)
        dyn_array.delete(9)
        self.assertEqual(dyn_array.count, 9)
        self.assertEqual(dyn_array.capacity, 16)

    def test_delete_buffer_exceeded(self):
        dyn_array = DynArray()
        for i in range(60):
            dyn_array.append(i)
        for j in range(59, 30, -1):
            dyn_array.delete(j)
        self.assertEqual(dyn_array.count, 31)
        self.assertEqual(dyn_array.capacity, 42)

    def test_delete_index_error(self):
        dyn_array = DynArray()
        for i in range(16):
            dyn_array.append(i)
        with self.assertRaises(IndexError) as context:
            dyn_array.delete(32)
        self.assertTrue('Index is out of bounds' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
