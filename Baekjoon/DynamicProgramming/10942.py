"""
펠린드롬?
"""
import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

m = int(input())

dp = [[0]*n for _ in range(n)]

for i in range(n):
    for start in range(n-i):
        end = start + i


        # 시작점과 끝점이 같으면 글자수가 1개이므로 무조건 펠린드롬이다.
        if start == end:
            dp[start][end] = 1

        elif nums[start] == nums[end]:
            if start + 1 == end:
                dp[start][end] = 1

            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])