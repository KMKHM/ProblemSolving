"""
암호
문제: https://www.acmicpc.net/problem/1718
"""

origin, key = input().rstrip(), input().rstrip()

s = "abcdefghijklmnopqrstuvwxyz"

if len(key) < len(origin):
    while len(key) <= len(origin):
        key+=key

ans = ""

for i in range(len(origin)):
    if origin[i] == " ":
        ans += origin[i]
    else:
        ans += s[s.index(origin[i]) - s.index(key[i]) - 1]

print(ans)