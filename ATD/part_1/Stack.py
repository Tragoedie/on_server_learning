class Stack:
    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2
    PEEK_NIL = 0
    PEEK_OK = 1
    PEEK_ERR = 2

    def __init__(self):

        # скрытые поля
        self.stack = []  # основное хранилище стека
        self.peek_status = Stack.PEEK_NIL  # статус запроса peek()
        self.pop_status = Stack.POP_ERR  # статус команды pop()
        # интерфейс класса, реализующий АТД Stack

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            self.pop(-1)
            self.pop_status = Stack.POP_OK
        else:
            self.pop_status = Stack.POP_ERR

    def clear(self):
        self.stack = []  # пустой список/стек

    # начальные статусы для предусловий peek() и pop()
    def peek(self):
        if self.size() > 0:
            result = self.stack[-1]
            self.peek_status = Stack.PEEK_OK
        else:
            result = 0
            self.peek_status = Stack.PEEK_ERR
        return result

    def size(self):
        return len(self.stack)

    # запросы статусов
    def get_pop_status(self):
        return self.pop_status

    def get_peek_status(self):
        return self.peek_status
