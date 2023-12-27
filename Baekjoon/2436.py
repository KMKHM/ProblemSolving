"""
공약수
문제: https://www.acmicpc.net/problem/2436
"""
g, l = map(int, input().split())

tmp = 1e9

div = l // g

ans = [0, 0]

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

for a in range(1, int(div**0.5)+1):
    b = int(div/a)

    if div % a == 0 and gcd(a, b) == 1:
        if b - a < tmp:
            tmp = b-a
            ans[0], ans[1] = a*g, b*g

print(*ans)