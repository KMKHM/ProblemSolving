"""
스티커
문제: https://www.acmicpc.net/problem/9465
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    dp = [arr1, arr2]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue


    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))