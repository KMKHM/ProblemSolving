"""
쉬운 계단 수
문제: https://www.acmicpc.net/problem/10844
"""
n = int(input())

if n == 1:
    print(9)

else:
    ans = 8*n+(n-1)
    print(ans%1000000000)
