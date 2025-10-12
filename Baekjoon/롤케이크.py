"""
https://www.acmicpc.net/problem/16206
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

tens = []
others = []

for x in arr:
    if x < 10:
        continue
    if x % 10 == 0:
        tens.append(x)
    else:
        others.append(x)

res = 0

tens.sort()

for x in tens:
    k = x // 10
    need = k - 1
    if m >= need:
        res += k
        m -= need
    else:
        res += m
        m = 0
        break

if m > 0:
    for x in others:
        k = x // 10
        if m == 0:
            break
        use = min(m, k)
        res += use
        m -= use

print(res)