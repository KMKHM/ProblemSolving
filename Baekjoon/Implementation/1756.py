"""
피자 굽기
문제: https://www.acmicpc.net/problem/1756
"""
import sys

input = sys.stdin.readline

d, n = map(int, input().split())

oven = list(map(int, input().split()))

pizza = list(map(int, input().split()))

check = [0] * d

end = d - 1

for i in range(n):
    start = 0
    while start < end:
        if oven[start] >= pizza[i] and oven[end] >= pizza[i]:
            start += 1
            end -= 1
        elif oven[end] < pizza[i]:
            start += 1
        if end == start + 1 and oven[start] >= pizza[i]:
            if not check[start]:
                check[start] = i + 1
                end = start - 1
                break
            else:
                print(0)
                sys.exit(0)
    print(start)