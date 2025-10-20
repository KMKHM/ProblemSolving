"""
https://www.acmicpc.net/problem/1107
"""
import sys

input = sys.stdin.readline

n = int(input())

m = int(input())

arr = list(map(int, input().split()))

cur = 0

ls = list(int(i) for i in str(n))

for i in range(len(ls)-1):
    if ls[i] in arr:
        if ls[i+1] <= 5:
            cur += 1