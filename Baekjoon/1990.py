"""
소수팰린드롬
문제: https://www.acmicpc.net/problem/1990
"""
a, b = map(int, input().split())

if b > 10000000:
    b = 10000000

prime = [1] * (b+1)

for num in range(2, int(b**0.5) + 1):
    for i in range(num+num, b+1, num):
        if prime[num]:
            prime[i] = 0

for i in range(a, b+1):
    if prime[i] and str(i) == str(i)[::-1]:
        print(i)

print(-1)