def is_arguments_for_substr_correct(string, index, length):
    if length < 1 or index < 0 or index > len(string)-1 or len(string)-1 < index + length-1:
        return False
    return True


string = 'Sansa Stark'
end = len(string) - 1
print(is_arguments_for_substr_correct(string, -1, 0))
print(is_arguments_for_substr_correct(string, 0, -1))
print(is_arguments_for_substr_correct(string, end + 1, 0))
print(is_arguments_for_substr_correct(string, end, 5))
print(is_arguments_for_substr_correct(string, end, 1))
