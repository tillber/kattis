# https://open.kattis.com/problems/treirad

from operator import mul
from functools import reduce

numbers = []
max = int(input())

for i in range(1, max):
    t = (i, i + 1, i + 2)
    if reduce(mul, t) < max:
        numbers.append(t)
        continue
    break

print(len(numbers))
