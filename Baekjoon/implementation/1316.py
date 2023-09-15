"""
그룹 단어 체커
문제: https://www.acmicpc.net/problem/1316
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

def check(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            continue
        elif string[i] in string[i+1:]:
            return False
    return True





ans = 0

for _ in range(n):
    s = input().rstrip()
    if check(s):
        ans += 1

print(ans)
