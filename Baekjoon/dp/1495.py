"""
기타리스트
문제: https://www.acmicpc.net/problem/1495
"""
import sys

input = sys.stdin.readline

n, s, m = map(int, input().split())

nums = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    tmp1 = s + nums[i] if  (0 <= (s + nums[i]) <= m) else -1
    tmp2 = s - nums[i] if  (0 <= (s - nums[i]) <= m) else -1

    if tmp1 == -1 and tmp2 == -1:
        print(-1)
        print(dp)
        sys.exit(0)
    else:
        if tmp1 == -1:
            s = tmp2
            dp[i][0] += tmp2
        elif tmp2 == -1:
            s = tmp1
            dp[i][1] += tmp1
        else:
            dp[i][0] += tmp1
            dp[i][1] += tmp2


print(max(dp))