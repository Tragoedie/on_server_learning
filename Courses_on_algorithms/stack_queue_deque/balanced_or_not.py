from on_server_learning.Courses_on_algorithms.stack_queue_deque.Stack import *


def balance_check(line):
    stack = Stack()
    for i in range(len(line)):
        if line[i] == '(':
            stack.push(line[i])
        elif line[i] == ')':
            if stack.size() == 0:
                return False
            else:
                stack.pop()
    return stack.size() == 0


line_brackets_1 = '(()((())()))'
print(balance_check(line_brackets_1))  # True
line_brackets_2 = '(()()(()'
print(balance_check(line_brackets_2))  # False
line_brackets_3 = '())('
print(balance_check(line_brackets_3))  # False
line_brackets_4 = '))(('
print(balance_check(line_brackets_4))  # False
line_brackets_5 = '((())'
print(balance_check(line_brackets_5))  # False
line_brackets_6 = '(((()))((())))))))((((((()))'
print(balance_check(line_brackets_1))  # True
