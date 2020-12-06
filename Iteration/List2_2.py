class List2_2:
    def __iter__(self):
        return self

    def __init__(self, N, infinity):
        self.start = 1
        self.count = 0
        self.N = N
        self.infinity = infinity

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count <= self.N:
            return current
        if self.infinity:
            self.start = 2
            self.count = 1
            return 1
        else:
            raise StopIteration


for n in List2_2(0, False):
    print(n)
