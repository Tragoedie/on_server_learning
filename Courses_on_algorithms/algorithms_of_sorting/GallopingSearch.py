class BinarySearch:

    def __init__(self, array):
        self.arr = array
        self.Left = 0
        self.Right = len(self.arr) - 1
        self.search_off = False
        self.end = False

    def Step(self, N):
        if self.end is True:
            return
        if self.arr == []:
            self.end = True
            return
        center = (self.Left + self.Right) // 2
        if self.arr[center] == N:
            self.search_off = True
            self.end = True
            return
        elif N < self.arr[center]:
            self.Right = center - 1
        else:
            self.Left = center + 1
        if self.Right - self.Left == 0 and self.arr[self.Left] == N:
            self.search_off = True
            self.end = True
            return
        if self.Right - self.Left <= 1 and self.arr[self.Left] != N and self.arr[self.Right] != N:
            self.end = True
            return

    def GetResult(self):
        if self.search_off is True:
            return 1
        if self.end is True:
            return -1
        return 0


def GallopingSearch(array, N):
    i = 1
    index = 2 ** i - 2
    while index <= len(array) - 1 and array[index] <= N:
        if array[index] == N:
            return True
        else:
            i += 1
            index = 2 ** i - 2
    if index > len(array) - 1:
        index = len(array) - 1
    binary = BinarySearch(array)
    binary.Left = (2 ** (i - 1) - 2) + 1
    binary.Right = index
    while binary.GetResult() == 0:
        binary.Step(N)
    if binary.GetResult() == 1:
        return True
    else:
        return False
