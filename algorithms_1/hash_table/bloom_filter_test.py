from on_server_learning.algorithms_1.hash_table.bloom_filter import BloomFilter

bloom_array = BloomFilter(32)
bloom_array.add('0123456789')
bloom_array.add('1234567890')
bloom_array.add('2345678901')
bloom_array.add('3456789012')
bloom_array.add('4567890123')
bloom_array.add('5678901234')
bloom_array.add('6789012345')
bloom_array.add('7890123456')
bloom_array.add('8901234567')
bloom_array.add('9012345678')

print(bloom_array.is_value('1234567890'))  # True
print(bloom_array.is_value('4567890123'))  # True
print(bloom_array.is_value('7890123456'))  # True
print(bloom_array.is_value('7777777777'))  # False
print(bloom_array.print_all())
