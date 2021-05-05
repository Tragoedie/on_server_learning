class BinarySearch:

    def __init__(self, array):
        self.arr = array
        self.Left = 0
        self.Right = len(self.arr) - 1
        self.search_off = False
        self.end = False

    def Step(self, N):
        center = (self.Left + self.Right) // 2
        if len(self.arr) == 0 or (len(self.arr) == 1 and self.arr[0] != N):
            self.end = True
        if self.end:
            return
        if self.arr[center] == N:
            self.search_off = True
            self.end = True
            return
        elif N < self.arr[center]:
            self.arr = self.arr[0:center]
        else:
            self.arr = self.arr[center + 1:]
        self.Right = len(self.arr) - 1
        self.Step(N)

    def GetResult(self):
        if self.search_off:
            return 1
        if self.end:
            return -1
        return 0
