"""
단어 수학
문제: https://www.acmicpc.net/problem/1339
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

words = [input().rstrip() for _ in range(n)]

words.sort(key=lambda x: len(x), reverse=True)

dic = Counter()

check = [0] * 10
def backtracking(level, val, cur):
    # Base condition
    if cur == 0:
        return

    for i in range(n):
        for j in range(len(words[i])):
            if words[i][j] not in dic and not check[cur]:
                dic[words[i][j]] = cur
                check[cur] = 1
                backtracking(level + 1, val + 1, cur-1)
                check[cur] = 0
                dic[words[i][j]] = 0


