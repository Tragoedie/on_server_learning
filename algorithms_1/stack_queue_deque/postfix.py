from on_server_learning.algorithms_1.stack.Stack import *


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def evaluation_of_postfix_expressions(st_1):
    st_2 = Stack()
    while st_1.size() > 0:
        symbol = st_1.pop()
        if is_number(symbol) is True:
            st_2.push(symbol)
        else:
            number_1 = st_2.pop()
            number_2 = st_2.pop()
            result = 0
            if symbol == '+':
                result = number_1 + number_2
            elif symbol == '-':
                result = number_1 - number_2
            elif symbol == '*':
                result = number_1 * number_2
            elif symbol == '/':
                result = number_1 / number_2
            if symbol == '=':
                return number_1
            st_2.push(result)
    return st_2.pop()


stack = Stack()
stack.push('=')
stack.push('+')
stack.push(9)
stack.push('*')
stack.push(5)
stack.push('+')
stack.push(2)
stack.push(8)
stack.print_all()
result = evaluation_of_postfix_expressions(stack)
print(result)

