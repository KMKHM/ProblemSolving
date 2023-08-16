"""
등수 매기기
문제: https://www.acmicpc.net/problem/2012
"""
import sys

input = sys.stdin.readline

n = int(input())

check = [i for i in range(1, n+1)]
nums = [int(input()) for _ in range(n)]
nums.sort()

ans = 0

for i in range(n):
    ans += abs(check[i]-nums[i])

print(ans)