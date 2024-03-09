"""
수열
https://www.acmicpc.net/problem/2491
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp_i, dp_d = [0] * n, [0] * n

dp_i[0], dp_d[0] = 1, 1

ans = 0

for i in range(1, n):
    for j in range(i):
        if nums[i] >= nums[j]:
            dp_i[i] = max(dp_i[i], dp_i[j] + 1)
        if nums[i] <= nums[j]:
            dp_d[i] = max(dp_d[i], dp_d[j] + 1)


print(dp_i)
print(dp_d)

