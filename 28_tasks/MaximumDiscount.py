def MaximumDiscount(N, price):
    x_change = True
    while x_change:
        x_change = False
        for i in range(N - 1):
            if price[i] < price[i + 1]:
                price[i], price[i + 1] = price[i + 1], price[i]
                x_change = True
    print(price)
    sum_discount = 0
    for j in range(N):
        if (j + 1) % 3 == 0:
            sum_discount += price[j]
    return sum_discount


# print(MaximumDiscount(9, [100, 350, 200, 250, 300, 150, 400, 100, 100]))
