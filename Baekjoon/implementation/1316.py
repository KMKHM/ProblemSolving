"""
그룹 단어 체커
문제: https://www.acmicpc.net/problem/1316
"""
import sys

input = sys.stdin.readline

n = int(input())

ans = 0

def check(string):
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            continue
        elif string[i] in string[i+1:]:
            return False
    return True


for _ in range(n):
    s = input().rstrip()
    if check(s):
        ans += 1

print(ans)
