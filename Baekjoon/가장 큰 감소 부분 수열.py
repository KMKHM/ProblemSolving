"""
https://www.acmicpc.net/problem/17216
"""
import sys

input = sys.stdin.readline

n=int(input())

arr=list(map(int, input().split()))

dp=[arr[i] for i in range(n)]
res=max(arr)
for i in range(n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i]=max(dp[j] + arr[i], dp[i])
            res=max(res, dp[i])
print(res)