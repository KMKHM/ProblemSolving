"""
N과 M (12)
문제: https://www.acmicpc.net/problem/15666
"""
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())

nums = sorted(list(map(int, input().split())))

check = [0] * n

res, tmp = [], []

def bt(level, idx):

    if level == m:
        if tmp not in res:
            res.append(tmp[:])
        return

    for i in range(idx, n):
        tmp.append(nums[i])
        bt(level + 1, i)
        tmp.pop()

bt(0, 0)

for r in res:
    print(*r)
