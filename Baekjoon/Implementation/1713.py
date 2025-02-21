"""
후보 추천하기
문제: https://www.acmicpc.net/problem/1713
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

m = int(input())

nums = list(map(int, input().split()))

dic = Counter()

check = [0] * 1001
stack = []
for i in range(m):
    dic[nums[i]] += 1
    if len(dic) > n:
        continue

