class ksort:

    def __init__(self):
        self.items = [None] * 800

    def index(self, s):
        if self.__help_add(s):
            index_s = int((str(ord(s[0]) - 97)) + s[1] + s[2])
            return index_s
        return -1

    def add(self, s):
        index_str = self.index(s)
        if index_str == -1:
            return False
        self.items[index_str] = s
        return True

    def __help_add(self, s):
        return len(s) == 3 and s[0] in 'abcdefgh' and s[1].isdigit() and s[2].isdigit()

    def print(self):
        for item in self.items:
            if item is not None:
                print(item, end=' ')

