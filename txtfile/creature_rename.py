import os
import random
for i in range(1, 11):

    list = open('list.txt', 'w')
    for y in range(3):
        x = random.randint(-1000, 1000)
        list.write(str(x)+"\n")
    list.close()
    os.rename('list.txt', str(i)+".txt")
