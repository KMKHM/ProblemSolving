"""
Dance Dance Revolution
문제: https://www.acmicpc.net/problem/2342
"""
import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

n=len(nums)

nums = nums[:n-1]

dp = [0]*n


# 한 발로만 하는 경우
# 두 발로만 하는 경우

dic = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}

cur = [0, 0]

for i in range(n):
    if 0 in cur:
        dp[i] = 2
        cur[cur.index(0)] += nums[i]
    else:
        if nums[i] in cur:
            dp[i] += 1
        elif nums[i] in dic[cur[0]] or nums[i] in dic[cur[1]]:
            continue
        # else:
print(dp)