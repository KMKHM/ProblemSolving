"""
https://www.acmicpc.net/problem/17393
"""
import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = [0] * n

for i in range(n-1):
    left = i
    right = n - 1
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        if b[mid] <= a[i]:
           cnt = mid
           left = mid + 1
        else:
            right = mid - 1
    res[i] = cnt - i

print(*res)