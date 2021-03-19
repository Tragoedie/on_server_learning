class aBST:

    def __init__(self, depth):
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        index = 0
        while index < len(self.Tree):
            if self.Tree[index] is None:
                return -index
            elif self.Tree[index] == key:
                return index
            elif key > self.Tree[index]:
                index = 2 * index + 2
            elif key < self.Tree[index]:
                index = 2 * index + 1
        return None

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        else:
            index = abs(index)
            self.Tree[index] = key
            return index
