import random


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        hash = 0
        for pos in key:
            hash += ord(pos) % self.size
        return hash % self.size

    def is_key(self, key):
        if self.get(key) is not None:
            return True
        return False

    def cleaning_slots(self):
        massive_min = []
        min_value = self.hits[self.hits.index(min(self.hits))]
        for i in range(len(self.hits)):
            if self.hits[i] == min_value:
                massive_min.append(i)
        if len(massive_min) > 1:
            index = massive_min[random.randint(0, len(massive_min))]
        else:
            index = massive_min[0]
        return index

    def put(self, key, value):
        slot = self.hash_fun(key)
        index = slot
        while self.slots[index] is not None and self.slots[index] != key:
            index = self.next_index(index)
            if index == slot:
                index = self.cleaning_slots()
                break
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] = 0

    def next_index(self, hash_old):
        return (hash_old + 2) % self.size

    def get(self, key):
        slot = self.hash_fun(key)
        index = slot
        while self.slots[index] is not None:
            if self.slots[index] == key:
                self.hits[index] += 1
                return self.values[index]
            index = self.next_index(index)
            if index == slot:
                break
        return None

    def remove_key(self, key):
        index = self.slots.index(key)
        self.slots[index] = None
        self.values[index] = None
        self.hits[index] = 0

    def cleaning_all_cache(self):
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def print_all(self):
        for i in range(self.size):
            print(self.slots[i])
            print(self.values[i])
            print(self.hits[i])

