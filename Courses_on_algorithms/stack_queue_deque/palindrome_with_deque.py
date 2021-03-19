from on_server_learning.algorithms_1.stack_queue_deque.deque_linked_list import *


def palindrome_or_not(line):
    deque = Deque()
    line = list(line)
    for i in range(len(line)):
        deque.addTail(line[i])
    while deque.size() > 1:
        if deque.removeTail() != deque.removeFront():
            return False
    return True


line_1 = '123454321'
print(palindrome_or_not(line_1))  # True
line_2 = '12344321'
print(palindrome_or_not(line_2))  # True
line_3 = '1'
print(palindrome_or_not(line_3))  # True
line_4 = '12345544321'
print(palindrome_or_not(line_4))  # False
line_5 = ''
print(palindrome_or_not(line_5))  # True
