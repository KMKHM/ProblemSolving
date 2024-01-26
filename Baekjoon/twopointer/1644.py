"""
소수의 연속합
문제: https://www.acmicpc.net/problem/1644
"""
import sys

n = int(input())

if n == 0 or n == 1:
    print(0)
    sys.exit(0)

nums = [1] * (n+1)

for i in range(2, int(n**0.5)+1):
    if nums[i]:
        for j in range(i*i, n+1, i):
            nums[j] = 0

temp = [i for i in range(2, n+1) if nums[i] == 1]

ans = 0 if nums[n] == 0 else 1

for i in range(len(temp)-1):

    start, end = i, i+1
    val = temp[start]

    while True:
        if end > n-1 or val > n:
            break

        val += temp[end]

        if val == n:
            ans += 1
            break

        elif val < n:
            end += 1


print(ans)