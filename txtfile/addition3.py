from txtfile.get_file_sum import get_file_sum


def addition(number_1, number_2):
    sum_1 = get_file_sum(number_1)
    sum_2 = get_file_sum(number_2)
    sum_common = sum_1 + sum_2
    return sum_common
