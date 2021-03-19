class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        hash = 0
        for pos in key:
            hash += ord(pos) % self.size
        return hash % self.size

    def is_key(self, key):
        if self.get(key) is not None:
            return True
        return False

    def put(self, key, value):
        slot = self.hash_fun(key)
        index = slot
        while self.slots[index] is not None and self.slots[index] != key:
            index = self.next_index(index)
            if index == slot:
                return None
        self.slots[index] = key
        self.values[index] = value

    def next_index(self, hash_old):
        return (hash_old + 2) % self.size

    def get(self, key):
        slot = self.hash_fun(key)
        index = slot
        while self.slots[index] is not None:
            if self.slots[index] == key:
                return self.values[index]
            index = self.next_index(index)
            if index == slot:
                break
        return None
