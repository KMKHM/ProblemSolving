"""
1, 2, 3 더하기 2
문제: https://www.acmicpc.net/problem/12101
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = [1, 2, 3]

tmp = []

cnt = 0

def bt(level):
    global cnt

    if level > n:
        return

    if sum(tmp) == n:
        cnt += 1
        if cnt == k:
            a = str(tmp[0])
            for i in tmp[1:]:
                a += "+"+str(i)
            print(a)
            sys.exit(0)
        return

    for i in range(3):
        tmp.append(nums[i])
        bt(level+1)
        tmp.pop()

bt(0)
print(-1)
