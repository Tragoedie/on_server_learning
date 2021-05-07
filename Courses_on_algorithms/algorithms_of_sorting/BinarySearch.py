class BinarySearch:

    def __init__(self, array):
        self.arr = array
        self.Left = 0
        self.Right = len(self.arr) - 1
        self.search_off = False
        self.end = False

    def Step(self, N):
        center = (self.Left + self.Right) // 2
        if self.arr == [] or (self.Right - self.Left <= 1 and self.arr[center] != N):
            self.end = True
            return
        if self.arr[center] == N:
            self.search_off = True
            self.end = True
            return
        elif N < self.arr[center]:
            self.Right = center - 1
        else:
            self.Left = center + 1

    def GetResult(self):
        if self.search_off is True:
            return 1
        if self.end is True:
            return -1
        return 0
