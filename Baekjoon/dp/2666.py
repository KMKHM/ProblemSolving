"""
벽장문 이동
문제: https://www.acmicpc.net/problem/2666
"""
import sys

input = sys.stdin.readline

n = int(input())

a, b = map(int, input().split())


t = int(input())

dp = [[0] * 2 for _ in range(t)]

ans = 0

for i in range(t):
    num = int(input())
    val1, val2 = abs(num-a), abs(num-b)

    dp[i][0] = 1
    dp[i][1] = 1


    if val1 > val2:
        ans += val2
        b = num
    else:
        ans += val1
        a = num

print(ans)