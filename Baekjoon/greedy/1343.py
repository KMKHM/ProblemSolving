"""
폴리노미오
문제: https://www.acmicpc.net/problem/1343
"""
s = input().rstrip()

s = s.replace("XXXX", "AAAA")
s = s.replace("XX", "BB")

if "X" in s:
    print(-1)
else:
    print(s)


