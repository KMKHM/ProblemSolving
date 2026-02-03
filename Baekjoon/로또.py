"""
https://www.acmicpc.net/problem/6603
"""

import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1:
        break

    for e in sorted(combinations(nums[1:], 6)):
        print(*e)
    print()