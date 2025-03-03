"""
부동산 다툼
문제: https://www.acmicpc.net/problem/20364
"""
import sys

input = sys.stdin.readline

n, q = map(int, input().split())

parent = [0] * (n+1)

# 부모 테이블
for i in range(1, n+1):
    l, r = i * 2, i * 2 + 1
    if l <= n:
        parent[l] = i
    if r <= n:
        parent[r] = i

check = [0] * (n+1)
check[1] = 1

track = []
def find(v):
    if v == parent[v]:
        return v
    track.append(v)
    return find(parent[v])

for _ in range(q):
    v = int(input())
    find(v)
    tmp = track[::-1][1:]

    flag = 1

    for t in tmp:
        if check[t]:
            print(t)
            flag = 0
            break
    if flag:
        check[v] = 1
        print(0)

    track = []
