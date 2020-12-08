import random
import time
from threading import Thread


def create_list(len_list):
    list_number = []
    for i in range(len_list):
        list_number.append(random.randint(-100, 100))
    return list_number


def for_counter(j, massive, N, res):
    sum = 0
    for i in range(j, len(massive), N):
        sum += massive[i]
        time.sleep(0.05)
    res.append(sum)


def counter(massive, N, results):
    for j in range(N):
        count_number = 'Count №' + str(j+1)
        t = Thread(target=for_counter, name=count_number, args=(j, massive, N, results))
        t.start()
    while t.is_alive():
        time.sleep(0.1)