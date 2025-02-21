"""
부등호
문제: https://www.acmicpc.net/problem/2529
"""
import sys
input = sys.stdin.readline

n = int(input())

s = input().split()

res = []

visited = [0] * 10

def check(a, b, o):
    if o == '<':
        if a > b:
            return False
    if o == '>':
        if a < b:
            return False
    return True

def bt(level, num):

    if level == n + 1:
        res.append(num)
        return

    for i in range(10):
        if (level == 0 or check(num[level-1], str(i), s[level-1])) and not visited[i]:
            visited[i] = 1
            bt(level + 1, num + str(i))
            visited[i] = 0

bt(0, "")
res.sort()
print(res[-1])
print(res[0])




