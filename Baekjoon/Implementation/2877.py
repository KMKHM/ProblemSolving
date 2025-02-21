"""
4와 7
문제: https://www.acmicpc.net/problem/2877
"""
import sys
from itertools import product

k = int(input())

nums = ["4", "7"]
# 4, 7 => 2
# 44, 47, | 74, 77 => 4
# 444, 447, 474, 477 | 744, 747, 774, 777 => 8
# 4444, 4447, 4474, 4477, 4744, 4747, 4774, 4777 | 7444, 7447, 7474, 7477, 7744, 7747, 7774, 7777 => 16

tmp, bi = 2, 1

while True:
    if tmp ** bi >= k:
        break
    bi += 1
print(bi)




# a = list(product(nums, repeat=num))
# print(tmp)
# print(order)
