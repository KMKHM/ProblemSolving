"""
수열과 쿼리 21
문제: https://www.acmicpc.net/problem/16975
"""
import sys
from math import *

input = sys.stdin.readline

n = int(input())

# 세그먼트 트리 인덱스
h = 2 << int(ceil(log(n, 2))) + 1

# 세그먼트 트리
tree = [0] * h

# 수열
arr = list(map(int, input().split()))

# 트리 초기화
def init_min(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]

    mid = (start + end) // 2
    init_min(start, mid, index * 2)
    init_min(mid+1, end, index * 2 + 1)

init_min(0, n-1, 1)

def update(start, end, left, right, index, value):
    if left > end or right < start:
        return
    if left <= start and right >= end:
        tree[index] += value
        return
    mid = (left + right) // 2
    update(start, mid, left, right, index * 2, value)
    update(mid + 1, end, left, right, index * 2 + 1, value)


