"""
https://www.acmicpc.net/problem/2168
"""
import math

x, y = map(int, input().split())

if x == y:
    print(x)
    exit(0)

print(x + y - math.gcd(x, y))