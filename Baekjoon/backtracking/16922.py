"""
로마 숫자 만들기
문제: https://www.acmicpc.net/problem/16922
"""
import sys
sys.setrecursionlimit(10**8)

n = int(input())

nums = [1, 5, 10, 50]

ans, tmp = set(), []

def bt(level, idx):
    global ans

    if level == n:
        ans.add(sum(tmp))
        return

    for i in range(idx, 4):
        tmp.append(nums[i])
        bt(level + 1, i)
        tmp.pop()

bt(0, 0)

print(len(ans))