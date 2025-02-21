"""
IPv6
문제: https://www.acmicpc.net/problem/3107
"""
s = input().rstrip().split(":")

n, m = 8, 4

if '' in s:
    if len(s) > n:
        while len(s) > n:
            del s[s.index('')]
    while True:
        if len(s) == n:
            break
        s.insert(s.index(''), '0000')

for i in range(n):
    if len(s[i]) < m:
        s[i] = s[i].zfill(m)

print(":".join(s))
