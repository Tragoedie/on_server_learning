def palindrome(word, begin, end):
    if end == 0:
        end = len(word) - 1
    if begin >= end:
        return True
    if word[begin] != word[end]:
        return False
    begin = begin + 1
    end = end - 1
    return palindrome(word, begin, end)


def palindromes(word):
    if not word:
        return True
    else:
        return word[0] == word[-1] and palindromes(word[1:-1])


# print(palindromes("арозаупаланалапуазора"))
# print(palindrome("арозаупаланалапуазора", 0, 0))
# print(palindromes("арозаупаланаалапуазора"))
# print(palindrome("арозаупаланаалапуазора", 0, 0))
# print(palindromes('a'))
# print(palindrome('a', 0, 0))
# print(palindromes(''))
# print(palindrome('', 0, 0))

