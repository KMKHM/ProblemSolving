"""
영단어 암기는 괴로워
문제: https://www.acmicpc.net/problem/20920
"""
import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

words = Counter()

for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    words[word] += 1

a = list(words.keys())

a.sort(key=lambda x: (-words[x], -len(x), x))

for s in a:
    print(s)




