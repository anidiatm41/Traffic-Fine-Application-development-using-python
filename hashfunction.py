class MyHashTable:

    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def get_slot(self, key):
        slot = self.hash_function(key)
        while self.keys[slot] and self.keys[slot] != key:
            slot = self.hash_function(slot + 1)
        return slot

    def set(self, key, value):
        slot = self.get_slot(key)
        self.keys[slot] = key
        self.values[slot] = value

    def get(self, key):
        return self.values[self.get_slot(key)]

    def destroy(self):
        self.keys = None
        self.values = None
        self.size = 0

