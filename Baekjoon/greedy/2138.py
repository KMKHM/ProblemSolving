"""
전구와 스위치
문제: https://www.acmicpc.net/problem/2138
"""
import sys

input = sys.stdin.readline

n = int(input())

target = list(input())

cur = list(input())

ans = 0

while cur != target:
    for i in range(n):
        if cur[i] == target[i]:
            continue

        if i == 0:
            cur[i] = "0" if cur[i] == "1" else "1"
            cur[i+1] = "0" if cur[i+1] == "1" else "1"
            ans += 1

        elif i == n-1:
            cur[i] = "0" if cur[i] == "1" else "1"
            cur[i - 1] = "0" if cur[i-1] == "1" else "1"
            ans += 1

        else:
            cur[i] = "0" if cur[i] == "1" else "1"
            cur[i + 1] = "0" if cur[i + 1] == "1" else "1"
            cur[i - 1] = "0" if cur[i - 1] == "1" else "1"
            ans += 1


print(ans)