"""
최소 힙
문제: https://www.acmicpc.net/problem/1927
"""
import sys, heapq

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)