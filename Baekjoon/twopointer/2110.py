"""
공유기 설치
문제: https://www.acmicpc.net/problem/2110
"""
import sys

input = sys.stdin.readline

n, c = map(int, input().split())

home = [int(input()) for _ in range(n)]
home.sort()

check = [0] * n
# 공유기 2대 설치
check[0], check[n-1] = 1, 1
c -= 2

if c == 2:
    print(home[n-1] - home[0])
    sys.exit(0)


left, right = 0, n-1

def bs(l, r):
    value, k = 0, 0
    while l < r:
        m = (l + r) // 2
        temp = home[m]
        temp_left, temp_right = home[l], home[r]

        if temp_right - temp >= temp - temp_left:
            if temp_right - temp > value:
                value = temp_right
                k = m

        if temp - temp_left > temp_right - temp:
            if temp_right - temp > value:
                value = temp_right
                k = m