"""
최솟값과 최댓값
https://www.acmicpc.net/problem/2357
"""
import sys
from math import *

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

h = int(ceil(log(n, 2)))
limit = 1 << (h+1)

tree_min = [0] * limit
tree_max = [0] * limit

def init_min(start, end, index):
    if start == end:
        tree_min[index] = arr[start]
        return tree_min[index]

    mid = (start + end) // 2
    tree_min[index] = min(init_min(start, mid, index * 2), init_min(mid+1, end, index * 2 + 1))
    return tree_min[index]
def init_max(start, end, index):
    if start == end:
        tree_max[index] = arr[start]
        return tree_max[index]

    mid = (start + end) // 2
    tree_max[index] = max(init_max(start, mid, index * 2), init_max(mid+1, end, index * 2 + 1))
    return tree_max[index]

init_min(0, n - 1, 1)
init_max(0, n - 1, 1)

def interval_min(start, end, index, left, right):
    if left > end or right < start:
        return 1000000001
    if left <= start and right >= end:
        return tree_min[index]
    mid = (start + end) // 2
    return min(interval_min(start, mid, index * 2, left, right), interval_min(mid + 1, end, index * 2 + 1, left, right))
def interval_max(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree_max[index]
    mid = (start + end) // 2
    return max(interval_max(start, mid, index * 2, left, right), interval_max(mid + 1, end, index * 2 + 1, left, right))

for _ in range(m):
    a, b = map(int, input().split())
    print(interval_min(0, n-1, 1, a-1, b-1), interval_max(0, n-1, 1, a-1, b-1))