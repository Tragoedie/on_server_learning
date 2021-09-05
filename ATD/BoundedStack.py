class BoundedStack:
    # константы
    STATUS_PUSH_NIL = 0  # push() еще не вызывалась
    STATUS_PUSH_OK = 1  # последняя push() отработала нормально
    STATUS_PUSH_ERR = 2  # последняя push() отработала некорректно - стек переполнен
    STATUS_POP_NIL = 0  # pop() ещё не вызывалась
    STATUS_POP_OK = 1  # последняя pop() отработала нормально
    STATUS_POP_ERR = 2  # стек пуст
    STATUS_PEEK_NIL = 0  # peek() ещё не вызывалась
    STATUS_PEEK_OK = 1  # последняя peek() вернула корректное значение
    STATUS_PEEK_ERR = 2  # стек пуст

    # конструктор:
    # предусловие: опция max_length, размер по умолчанию = 32
    # постусловие: создан новый пустой стек
    def __init__(self, max_length=32):
        # скрытые поля
        self.stack = []  # основное хранилище стека
        # максимальный размер
        self.max_length = max_length  # максимальный размер стека
        # статусы
        self.push_status = BoundedStack.STATUS_PUSH_NIL  # статус запроса push()
        self.peek_status = BoundedStack.STATUS_PEEK_NIL  # статус запроса peek()
        self.pop_status = BoundedStack.STATUS_POP_ERR  # статус команды pop()

    # команды:
    # предусловие: размер стека меньше max_length (стек еще не полон);
    # постусловие: в стек добавлено новое значение;
    def push(self, value):
        if self.size() < self.max_length:
            self.stack.append(value)
            self.push_status = BoundedStack.STATUS_PUSH_OK
        else:
            self.push_status = BoundedStack.STATUS_PUSH_ERR

    # предусловие: стек не пустой;
    # постусловие: из стека удалён верхний элемент;
    def pop(self):
        if self.size() > 0:
            self.pop(-1)
            self.pop_status = BoundedStack.STATUS_POP_OK
        else:
            self.pop_status = BoundedStack.STATUS_POP_ERR

    # постусловие: из стека удалятся все значения и обновляются статусы;
    def clear(self):
        self.stack = []  # пустой список/стек;
        self.push_status = BoundedStack.STATUS_PUSH_NIL
        self.peek_status = BoundedStack.STATUS_PEEK_NIL
        self.pop_status = BoundedStack.STATUS_POP_ERR

    # запросы:
    # предусловие: стек не пустой
    def peek(self):
        if self.size() > 0:
            result = self.stack[-1]
            self.peek_status = BoundedStack.STATUS_PEEK_OK
        else:
            result = 0
            self.peek_status = BoundedStack.STATUS_PEEK_ERR
        return result

    def size(self):
        return len(self.stack)

    # дополнительные запросы:
    def get_push_status(self):  # возвращает значение PUSH_*
        return self.push_status

    def get_pop_status(self):  # возвращает значение POP_*
        return self.pop_status

    def get_peek_status(self):  # возвращает значение PEEK_*
        return self.peek_status

    def get_max_length(self):  # возвращает значение максимальной длины
        return self.max_length
