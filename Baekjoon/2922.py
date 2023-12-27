"""
즐거운 단어
문제: https://www.acmicpc.net/problem/2922
"""
import sys

input = sys.stdin.readline

s = list(input().rstrip())


vowel = ["A", "E", "I", "O", "U"]

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

n = len(s)

def check(string):
    if "L" not in string:
        return False
    for i in range(len(string)-2):
        if string[i] in vowel and string[i+1] in vowel and string[i+2] in vowel:
            return False
        if string[i] not in vowel and string[i+1] not in vowel and string[i+2] not in vowel:
            return False
    return True

ans = 0

res = []
def backtracking(idx):
    global ans

    if idx == n:
        if check(s):
            ans += 1
            return
        return

    if s[idx] == "_":
        for a in alpha:
            s[idx] = a
            backtracking(idx + 1)
            s[idx] = "_"
    else:
        backtracking(idx + 1)


backtracking(0)

print(ans)