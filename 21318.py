"""
피아노 체조
문제: https://www.acmicpc.net/problem/21318
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

# 누적합 배열
prefix_sum = [0]*n

cnt = 0

# 누적합
for i in range(n-1):
    if nums[i+1] < nums[i]:
        cnt += 1
    prefix_sum[i+1] = cnt

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b-1] - prefix_sum[a-1])


