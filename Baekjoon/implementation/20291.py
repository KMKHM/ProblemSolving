"""
파일 정리
문제: https://www.acmicpc.net/problem/20291
"""
import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

n = int(input())

# 사전형
dic = Counter()

for _ in range(n):
    s = input().rstrip().split(".")
    dic[s[1]] += 1

key = sorted(dic.keys())

for k in key:
    print(k, dic[k])

print(dic2)