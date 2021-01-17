class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hash = 0
        for pos in value:
            hash += ord(pos) % self.size
        return hash % self.size

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        slot_seek = slot
        while self.slots[slot_seek] is not None:
            slot_seek = self.next_index(slot_seek)
            if slot_seek == slot:
                return None
        return slot_seek

    def next_index(self, hash_old):
        return (hash_old + self.step) % self.size

    def put(self, value):
        empty_slot = self.seek_slot(value)
        if empty_slot is not None:
            self.slots[empty_slot] = value
            return empty_slot
        return None

    def find(self, value):
        slot = self.hash_fun(value)
        slot_seek = slot
        while self.slots[slot_seek] is not None:
            if self.slots[slot_seek] == value:
                return slot_seek
            slot_seek = self.next_index(slot_seek)
            if slot_seek == slot:
                break
        return None
