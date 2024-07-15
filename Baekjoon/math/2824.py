"""
최대 공약수
문제: https://www.acmicpc.net/problem/2824
"""
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

A, B = 1, 1

for i in a:
    A *= i

for j in b:
    B *= j


def cal(x, y):
    while y > 0:
        tmp = x % y
        x = y
        y = tmp
    return x

print(str(cal(max(A, B), min(A, B)))[-9:])