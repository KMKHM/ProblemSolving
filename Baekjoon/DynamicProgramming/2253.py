"""
점프
문제: https://www.acmicpc.net/problem/2253
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 건널 수 없는 돌
impossible = [int(input()) for _ in range(m)]

dp = [0] * (n+1)

# 첫 번째는 한 칸만 점프
dp[2] = 1

if n == 2:
    print(1)
    sys.exit(0)

for i in range(3, n+1):
    # 만약 이전칸에 한 칸만 점프를 했다면 다음 칸은 1칸 또는 2칸만 점프할 수 있고 2칸을 점프했다면 123 중 하나를 점프할 수 있다.
    if i in impossible:
        continue

    if i-1 == 2 or i-2 == 2:
        for j in (i, i+1):
            dp[j] = dp[j-1] + 1


print(dp)