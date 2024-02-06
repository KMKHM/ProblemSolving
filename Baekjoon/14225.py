"""
부분수열의 합
문제: https://www.acmicpc.net/problem/14225
"""
import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

check = [0] * (sum(num)+2)

def bt(idx,sum):
    if idx == n:
       return
    sum += num[idx]
    check[sum] = 1
    bt(idx+1, sum)
    bt(idx+1, sum-num[idx])


bt(0, 0)

print(check[1:].index(0)+1)
