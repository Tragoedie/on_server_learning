class PowerSet:

    def __init__(self):
        self.slots = []

    def size(self):
        return len(self.slots)

    def put(self, value):
        if value not in self.slots:
            self.slots.append(value)

    def get(self, value):
        if value in self.slots:
            return True
        return False

    def remove(self, value):
        if value in self.slots:
            self.slots.remove(value)
            return True
        return False

    def intersection(self, set2):  # пересечение
        intersection_set = PowerSet()
        for i in self.slots:
            if set2.get(i) is True:
                intersection_set.put(i)
        return intersection_set

    def union(self, set2):  # объединение
        intersection_set = PowerSet()
        for i in set2.slots:
            intersection_set.put(i)
        for j in self.slots:
            intersection_set.put(j)
        return intersection_set

    def difference(self, set2):  # разница
        intersection_set = PowerSet()
        for i in self.slots:
            if set2.get(i) is False:
                intersection_set.put(i)
        return intersection_set

    def issubset(self, set2):
        for i in set2.slots:
            if self.get(i) is False:
                return False
        return True

    def print_all(self):
        for i in self.slots:
            print(i)

