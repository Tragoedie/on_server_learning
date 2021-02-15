def depth_result_array(a):
    depth_tree = 0
    len_tree = 0
    while len_tree < len(a):
        depth_tree += 1
        len_tree = 2 ** (depth_tree + 1) - 1
    return depth_tree


def GenerateBBSTArray(a):
    a.sort()
    depth = depth_result_array(a)
    result_array = [None] * (2 ** (depth + 1) - 1)
    recursive_generate(a, result_array, 0)
    return result_array


def recursive_generate(a, result_array, index):
    if len(a) > 0:
        index_center = len(a) // 2
        result_array[index] = a[index_center]
        recursive_generate(a[:index_center], result_array, 2 * index + 1)
        recursive_generate(a[index_center + 1:], result_array, 2 * index + 2)

