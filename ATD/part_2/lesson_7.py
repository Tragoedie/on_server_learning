class Parent:
    def __init__(self):
        pass

    number = 10

    def print_val(self):
        print(self.number)


class Child(Parent):
    number = 40


obj = Child()
obj.print_val()  # returns 40
