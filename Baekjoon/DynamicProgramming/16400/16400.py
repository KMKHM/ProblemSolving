"""
소수 화폐
문제: https://www.acmicpc.net/problem/16400
"""
import sys

input = sys.stdin.readline

n = int(input())

prime = [1] * (n+1)

for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = 0

mod = 123456789

dp = [0] * (n+1)

