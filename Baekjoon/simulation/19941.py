"""
햄버거 분해
문제: https://www.acmicpc.net/problem/19941
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

s = input().rstrip()

res = 0

check = [0] * n

for i in range(n):
    if s[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0<=j<n and not check[j] and s[j]=='H':
                check[j]=1
                res += 1
                break

print(res)
