"""
로프
문제: https://www.acmicpc.net/problem/2217
"""
import sys

input = sys.stdin.readline

n = int(input())

# 로프가 버틸 수 있는 최대 중량
nums = sorted(int(input()) for _ in range(n))

# 최대 중량
w = 0

# 개수
tmp = 0
for i in range(n):
    w = max(w, nums[i]*(n-tmp))
    tmp += 1
print(w)



