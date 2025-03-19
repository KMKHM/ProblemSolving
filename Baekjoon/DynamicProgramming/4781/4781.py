"""
사탕 가게
문제: https://www.acmicpc.net/problem/4781
"""
import sys

input = sys.stdin.readline

while True:
    a, b = input().split()

    if a == "0" and b == "0.00":
        break

    a = int(a)
    b = int(b * 100 + 0.5)

    cost, calorie = [0], [0]

    for _ in range(a):
        x, y = input().split()
        cost.append(int(y * 100 + 0.5))
        calorie.append(int(x))

    dp = [[0] * (b+1) for _ in range(a+1)]

    ans = 0

    for i in range(1, a+1):
        for j in range(1, b+1):
            if cost[i] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i]] + calorie[i]*(j // cost[i]))
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[a][b])
