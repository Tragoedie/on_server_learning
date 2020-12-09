import random
import time
from threading import Thread


def create_list(len_list):
    list_number = []
    for i in range(len_list):
        list_number.append(random.randint(-100, 100))
    return list_number


def for_counter(j, massive, N, results_massive):
    sum = 0
    for i in range(j, len(massive), N):
        sum += massive[i]
        time.sleep(0.05)
    results_massive.append(sum)


def counter(massive, N):
    results = {}
    results_massive = []
    for j in range(N):
        count_number = 'Count №' + str(j + 1)
        results[j] = Thread(target=for_counter, name=count_number, args=(j, massive, N, results_massive))
        results[j].start()
    xchange = True
    while xchange:
        xchange = False
        for value in results.values():
            if value.is_alive():
                xchange = True
        if xchange:
            time.sleep(0.05)
    print(results)
    total_sum_conc = 0

    for x in range(len(results_massive)):
        total_sum_conc += results_massive[x]
    return total_sum_conc
