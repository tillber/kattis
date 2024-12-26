# https://open.kattis.com/problems/sifferprodukt

from operator import mul
from functools import reduce


def multiply(num):
    if len(num) == 1:
        print(num)
        return
    digits = (x if x > 0 else 1 for x in map(int, list(num)))
    multiply(str(reduce(mul, digits)))


multiply(input())
