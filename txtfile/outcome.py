import random
from txtfile.addition2 import addition
number_1 = random.randint(1, 10)
print("Step 1 - Номер первого файла:", number_1)
number_2 = random.randint(1, 10)
print("Step 2 - Номер второго файла:", number_2)

print("Сумма чисел равна = ", addition(number_1, number_2))
