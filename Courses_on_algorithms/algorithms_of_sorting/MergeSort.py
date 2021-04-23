def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    center = len(arr) // 2
    arr_left = MergeSort(arr[:center])
    arr_right = MergeSort(arr[center:])

    return __merge_sort(arr_left, arr_right)


def __merge_sort(left, right):
    arr_result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            arr_result.append(left.pop(0))
        else:
            arr_result.append(right.pop(0))
    if len(left) > 0:
        arr_result.extend(left)
    if len(right) > 0:
        arr_result.extend(right)
    return arr_result



