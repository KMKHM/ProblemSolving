"""
나의 인생에는 수학과 함께
문제: https://www.acmicpc.net/problem/17265
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = [list(input().split()) for _ in range(n)]

dp1 = [[0]*n for _ in range(n)]
dp2 = [[0]*n for _ in range(n)]

dp1[0][0] = dp2[0][0] = int(arr[0][0])

def operation(x, y, s):
    if s == "+":
        return x + y
    elif s == "-":
        return x - y
    else:
        return x * y

# 세로
for i in range(2, n, 2):
    dp1[i][0] = dp2[i][0] = operation(dp1[i-2][0], int(arr[i][0]), arr[i-1][0])

# 가로
for i in range(2, n, 2):
    dp1[0][i] = dp2[0][i] = operation(dp1[0][i-2], int(arr[0][i]), arr[0][i-1])

for i in range(1, n):
    for j in range(1, n):
        if arr[i][j].isdigit():
            dp1[i][j] = max(operation(int(arr[i][j]), dp1[i-1][j-1], arr[i][j-1]), operation(int(arr[i][j]), dp1[i-1][j-1], arr[i-1][j]))
            dp2[i][j] = min(operation(int(arr[i][j]), dp2[i-1][j-1], arr[i][j-1]), operation(int(arr[i][j]), dp2[i-1][j-1], arr[i-1][j]))


print(dp1)
print(dp2)

for i in dp1:
    print(*i)