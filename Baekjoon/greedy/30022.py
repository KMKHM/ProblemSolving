"""
행사 준비
문제: https://www.acmicpc.net/problem/30022
"""
import sys, heapq

input = sys.stdin.readline

n, A, B = map(int, input().split())

q1, q2 = [], []

ans = 0

check = [0] * n

for i in range(n):
    x, y = map(int, input().split())
    heapq.heappush(q1, (x, i))
    heapq.heappush(q2, (y, i))

for _ in range(n):
    if q1[0][0] >= q2[0][0]:
        if not check[q2[0][1]]:
            p, idx = heapq.heappop(q2)
            check[idx] = 1
            ans += p
        else:
            p, idx = heapq.heappop(q1)
            check[idx] = 1
            ans += p
    else:
        if not check[q1[0][1]]:
            p, idx = heapq.heappop(q1)
            check[idx] = 1
            ans += p
        else:
            p, idx = heapq.heappop(q2)
            check[idx] = 1
            ans += p
print(ans)



