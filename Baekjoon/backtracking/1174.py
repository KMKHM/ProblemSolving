"""
줄어드는 수
문제: https://www.acmicpc.net/problem/1174
"""
import sys
from itertools import combinations

n = int(input())

# 반대로 정렬하면 이게 10자리수 # 9~0
nums = [str(i) for i in range(9, -1, -1)]


cnt = 0

for i in range(1, 11):
    tmp = sorted(list("".join(j) for j in combinations(nums, i)))
    for j in tmp:
        cnt += 1
        if cnt == n:
            print(j)
            sys.exit(0)


print(-1)




