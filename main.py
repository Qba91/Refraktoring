# -*- coding: UTF-8 -*-

"""
calculates the sum of the squares of digits, checked numbers.

Note:
    This function is a public function.

Args:
    number(int):    next checked number.

Returns:
    final(int): the sum of the squares of digits.

Example:
    >>> input 44 return --> 32
    >>> input 85 return --> 89
"""
def sum_of_square_of_digits(number):
    final = 0
    while number > 0:
        digit = number % 10
        final += digit * digit
        number //= 10
    return final


def sequence(num, cache):
    seq = []
    while num != 1 and num != 89:
        if num in cache:
            num = cache[num]
            break
        seq.append(num)
        num = sum_of_square_of_digits(num)
    for c in seq:
        cache[c] = num
    return num

cache = {}

print(sum([1 for i in range(1, 1000000) if sequence(i, cache) == 89]))
