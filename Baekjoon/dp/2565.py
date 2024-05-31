"""
전깃줄
문제: https://www.acmicpc.net/problem/2565
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
dp = [1] * n

def check(x, y):
    if x[0] == y[0] and x[1] == y[1]:
        return False
    if x[0] >= y[0] and x[1] >= y[1]:
        return True
    if x[0] <= y[0] and x[1] <= y[1]:
        return True


for i in range(1, n):
    for j in range(i):
        if check(arr[i], arr[j]):
            dp[i] = max(dp[j] + 1, dp[i])

# print(arr)
# print(dp)
print(n - max(dp))