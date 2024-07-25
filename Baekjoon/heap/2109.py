"""
순회 강연
문제: https://www.acmicpc.net/problem/2109
"""

import heapq

N = int(input())
lectures = []
for _ in range(N):
    p, d = map(int, input().split())
    lectures.append((d, p))

lectures.sort()
q = []

for lecture in lectures:
  d, p = lecture
  heapq.heappush(q, p)
  if len(q) > d:
    heapq.heappop(q)

print(sum(q))