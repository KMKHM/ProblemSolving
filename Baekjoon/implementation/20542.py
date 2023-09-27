"""
받아쓰기
문제: https://www.acmicpc.net/problem/20542
"""
import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

dic = {"i": ["j", "l"], "v": "w"}

# 받아쓴 것
sol = Counter(input().rstrip())
# 정답
origin = Counter(input().rstrip())



