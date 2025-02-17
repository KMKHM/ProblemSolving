"""
내려가기
문제: https://www.acmicpc.net/problem/2096
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

dp1 = dp2 = arr

for i in range(n-1):
    arr = list(map(int, input().split()))
    dp1 = [max(dp1[0], dp1[1]) + arr[0], max(dp1[0], dp1[1], dp1[2]) + arr[1], max(dp1[1], dp1[2]) + arr[2]]
    dp2 = [min(dp2[0], dp2[1]) + arr[0], min(dp2[0], dp2[1], dp2[2]) + arr[1], min(dp2[1], dp2[2]) + arr[2]]

print(max(dp1), min(dp2))