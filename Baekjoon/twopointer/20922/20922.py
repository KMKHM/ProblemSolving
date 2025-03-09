"""
겹치는 건 싫어
문제: https://www.acmicpc.net/problem/20922
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if n == 1:
    print(1)
    sys.exit(0)

nums = list(map(int, input().split()))

check = [0] * 100001

left, right = 0, 0

res = 0

while right < n:
    if check[nums[right]] < k:
        check[nums[right]] += 1
        right += 1
    else:
        check[nums[left]] -= 1
        left += 1

    res = max(res, right - left)

print(res)


