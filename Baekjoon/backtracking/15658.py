"""
연산자 끼워넣기 (2)
https://www.acmicpc.net/problem/15658
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

op = list(map(int, input().split()))

res1 = -sys.maxsize
res2 = sys.maxsize

def dfs(num, level):
    global res1, res2

    if level == n-1:
        res1 = max(res1, num)
        res2 = min(res2, num)
        return

    if op[0]:
        op[0] -= 1
        dfs(num + nums[level+1], level+1)
        op[0] += 1

    if op[1]:
        op[1] -= 1
        dfs(num - nums[level+1], level+1)
        op[1] += 1

    if op[2]:
        op[2] -= 1
        dfs(num * nums[level+1], level+1)
        op[2] += 1

    if op[3]:
        op[3] -= 1
        dfs(int(num / nums[level+1]), level+1)
        op[3] += 1

dfs(nums[0], 0)
print(res1)
print(res2)
