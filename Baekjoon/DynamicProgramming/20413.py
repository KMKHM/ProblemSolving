"""
MVP 다이아몬드 (Easy)
문제: https://www.acmicpc.net/problem/20413
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dic = dict(zip(["S", "G", "P", "D"], nums))

s = input().rstrip()

"""
0~29
30~59
60~89
90~149
150~ 
"""
# 29 + 30 + 59
start = 0
res = 0

for i in range(n):
    res += (dic[s[i]] - 1) - start
    start = (dic[s[i]] - 1) - start

print(res)
