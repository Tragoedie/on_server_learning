def summ(number):
    if number // 10 < 1:
        return number
    else:
        return number % 10 + summ(number // 10)


print(summ(123))
