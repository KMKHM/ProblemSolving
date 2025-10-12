"""
https://www.acmicpc.net/problem/1038
"""
from itertools import combinations

n = int(input())

if n <= 9:
    print(n)
    exit(0)
if n >= 1023:
    print(-1)
    exit(0)

res = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums = [i for i in range(9, -1, -1)]

for i in range(2, 11):
    temp = []
    for num in list(combinations(nums, i)):
        temp.append("".join(map(str, num)))
    temp.sort()
    res += temp

print(res[n])