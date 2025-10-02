"""
카드 합체 놀이
문제: https://www.acmicpc.net/problem/15903
"""
import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
heapq.heapify(arr)

while m:
    m -= 1
    x, y = heapq.heappop(arr), heapq.heappop(arr)
    heapq.heappush(arr, x+y)
    heapq.heappush(arr, x+y)

print(sum(arr))