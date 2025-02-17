"""
수강 과목
문제: https://www.acmicpc.net/problem/17845
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

subject = [[0, 0]] + [list(map(int, input().split())) for _ in range(k)]

dp = [[0, 0]] * (k+1)

for i in range(1, k):
    # 중요도, 시간
    w, t = subject[i][0], subject[i][1]
    w1, t1 = dp[i][0], dp[i][1]
    for j in range(i):
        # 최대 시간보다 작거나 같으면
        if subject[j][1] + t1 <= n:
            if w1 < dp[j][0] + dp[i][0] + w:
                dp[i][0] = w1 + dp[j][0] + w
                dp[i][1] = t1 + dp[j][1] + t

print(dp)


