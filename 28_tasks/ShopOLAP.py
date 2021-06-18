def CountNumOfIdentProducts(item_s, amount_s):
    change = False
    while change is False:  # count the number of identical products
        change = True
        for i in range(len(item_s) - 1):
            for j in range(1 + i, len(item_s)):
                if item_s[i] == item_s[j]:
                    change = False
                    amount_s[i][0] = int(amount_s[i][0]) + int(amount_s[j][0])
                    amount_s.pop(j)
                    item_s.pop(j)
                    break

def sort_quantity_asc(item_s, amount_s):
    change = False
    while change is False:  # sort quantity in ascending order
        change = True
        for i in range(len(amount_s) - 1):
            if amount_s[i] < amount_s[i + 1]:
                change = False
                amount_s[i], amount_s[i + 1] = amount_s[i + 1], amount_s[i]
                item_s[i], item_s[i + 1] = item_s[i + 1], item_s[i]

def sort_products_lexic_asc(item_s, amount_s):
    begin = 0
    end = 0
    for x in range(1, len(amount_s)):  # sorting products in lexicographic ascending order
        if amount_s[begin] == amount_s[x]:
            end = x
        if amount_s[begin] != amount_s[x] or end == len(amount_s) - 1:
            if end != 0:
                change = False
                while change is False:
                    for i in range(begin, end):
                        change = True
                        if item_s[i] > item_s[i + 1]:
                            item_s[i], item_s[i + 1] = item_s[i + 1], item_s[i]
                            change = False
                end = 0
            begin = x
def ShopOLAP(N, items):
    if N == 1:
        return items
    for a in range(len(items)):  # division into goods_array and quantity_array
        items[a] = list(items[a])
    item_s = []
    amount_s = []
    for x in range(len(items)):
        work_item = []
        amount_item = []
        change = False
        for y in range(len(items[x])):
            if items[x][y - 1] == ' ':
                change = True
            if change is False:
                work_item.append(items[x][y])
            else:
                amount_item.append(items[x][y])
        if len(amount_item) > 1:
            amount_items = amount_item
            amount_items = ''.join(amount_items)
            amount_items = int(amount_items)
            amount_item = [amount_items]
            amount_s.append(amount_item)
        else:
            amount_item = [int(amount_item[0])]
            amount_s.append(amount_item)
        item_s.append(work_item)
    CountNumOfIdentProducts(item_s, amount_s)
    sort_quantity_asc(item_s, amount_s)
    sort_products_lexic_asc(item_s, amount_s)
    result = []
    for i in range(len(amount_s)):  # creating the resulting string
        b = []
        item_s[i] = ''.join(item_s[i])
        amount_s[i] = str(amount_s[i][0])
        amount_s[i] = ''.join(amount_s[i])
        b.append(item_s[i])
        b.append(amount_s[i])
        b = ''.join(b)
        result.append(b)
    return result

# N = 2
# items = ['платье1 5', 'сумка32 6', 'платье3 5', 'платье2 5', 'сумка23 3', 'сумка128 2', 'сумка126 2']
# items = ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']
# items = ['платье1 5', 'платье1 5', 'платье1 5']
# print(ShopOLAP(N, items))
# print(ShopOLAP(8, ["123 5", "32 3", "124 5", "128 1", "32 2", "23 4", "128 4", "128 1"]))
