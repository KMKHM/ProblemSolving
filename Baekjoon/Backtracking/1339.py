import sys

input = sys.stdin.readline

n = int(input())

words = [input().rstrip() for _ in range(n)]

words.sort(reverse=True, key=lambda x: len(x))

depth = len(words[0])

dic = dict()

check = [0] * 9

answer = 0

def backtracking(level, val):

    global answer

    if level == depth:
        answer = max(answer, val)
        return

    for i in range(n):
        word = words[i]
        for j in range(len(word)):
            word[j]



