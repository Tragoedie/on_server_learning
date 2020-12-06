class List2_1:
    def __iter__(self):
        return self

    def __init__(self, start):
        self.start = start
        self.count = 0

    def __next__(self):
        current = self.start
        self.start = self.start * 2
        self.count += 1
        if self.count < 10:
            return current
        raise StopIteration


for n in List2_1(5):
    print(n)
