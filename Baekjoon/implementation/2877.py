"""
4와 7
문제: https://www.acmicpc.net/problem/2877
"""
n = int(input())

z = 2

while 1:
    if z <= n:
        z = z**2
    if z > n:
        break
print(z)