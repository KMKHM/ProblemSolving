"""
무한 문자열
문제: https://www.acmicpc.net/problem/12871
"""
s=input().rstrip()
t=input().rstrip()

tmp1, tmp2 = s, t

while len(s) != len(t):
    if len(s) < len(t):
        s+=tmp1
    elif len(s) > len(t):
        t+=tmp2

print(1 if s==t else 0)