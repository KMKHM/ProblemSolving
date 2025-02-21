"""
가르침
문제: https://www.acmicpc.net/problem/1062
"""
import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())

pre = set(["a", "n", "t", "i", "c"])

if len(pre) >= k:
    print(0)
    sys.exit(0)

possible = k - len(pre)

words = []

for _ in range(n):
    word = input().rstrip()
    word = word.replace("anta", "")
    word = word.replace("tica", "")
    words.append("".join(set(word)))

ans = 0

for i in range(n, 0, -1):
    tmp = list(combinations(words, i))
    for j in range(len(tmp)):
        s = set("".join(tmp[j])) - pre
        if len(s) <= possible:
            ans = max(i, ans)
            print(ans)
            sys.exit(0)






