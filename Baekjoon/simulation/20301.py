"""
타노스
문제: https://www.acmicpc.net/problem/20310
"""
s = list(input().rstrip())

o, z = s.count("1")//2, s.count("0")//2

for _ in range(o):
    s.remove("1")
s = s[::-1]
for _ in range(z):
    s.remove("0")

print("".join(s[::-1]))
