"""
회전 초밥
문제: https://www.acmicpc.net/problem/2531
"""
import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

nums = [int(input()) for _ in range(n)]

nums = nums + nums[:n-1]

# 7, 9, 7, 30, 2, 7, 9, 25, 7, 9, 7, 30, 2, 7, 9


# 최대 k + 1개

# 만약 쿠폰이 있는 초밥이 없다면 무조건 연속으로 먹고 쿠폰으로 새로 만들어 먹으면 되므로 k+1
if c not in nums:
    if n == k:
        print(n+1)
    else:
        print(k+1)
    sys.exit(0)

for i in range(n):
    tmp = nums[i:i+k]

    if c not in tmp:
        print(k + 1)
        sys.exit(0)
print(k)






