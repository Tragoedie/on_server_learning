class Heap:

    def __init__(self):
        self.HeapArray = []
        self.HeapArray_size = 0
        self.HeapArray_maxsize = 0

    def MakeHeap(self, a, depth):
        if a == []:
            return
        self.HeapArray_maxsize = (2 ** (depth + 1) - 1)
        self.HeapArray = [None] * self.HeapArray_maxsize
        array = sorted(a, reverse=True)
        for i in range(len(array)):
            self.HeapArray[i] = array[i]
            self.HeapArray_size += 1

    def GetMax(self):
        if self.HeapArray == []:
            return -1
        elem = self.HeapArray.pop(0)
        self.HeapArray_size = self.HeapArray_size - 1
        self.HeapArray.append(None)
        if self.HeapArray_size == 0:
            self.HeapArray = []
            return elem
        self.HeapArray.insert(0, self.HeapArray.pop(self.HeapArray_size-1))
        index = 0
        while 2 * index + 2 < self.HeapArray_size and self.HeapArray[index] < max(self.HeapArray[2 * index + 1], self.HeapArray[2 * index + 2]):
            if self.HeapArray[2 * index + 1] > self.HeapArray[2 * index + 2]:
                self.HeapArray[index], self.HeapArray[2 * index + 1] = self.HeapArray[2 * index + 1], self.HeapArray[index]
                index = 2 * index + 1
            else:
                self.HeapArray[index], self.HeapArray[2 * index + 2] = self.HeapArray[2 * index + 2], self.HeapArray[index]
                index = 2 * index + 2
        return elem

    def Add(self, key):
        if (self.HeapArray_size + 1) > self.HeapArray_maxsize:
            return False
        self.HeapArray_size += 1
        self.HeapArray[self.HeapArray_size - 1] = key
        index = self.HeapArray_size - 1
        while index > 0 and self.HeapArray[index] > self.HeapArray[(index - 1) // 2]:
            self.HeapArray[index], self.HeapArray[(index - 1) // 2] = self.HeapArray[(index - 1) // 2], self.HeapArray[index]
            index = (index - 1) // 2
        return True

