"""
연산자 끼워넣기
문제: https://www.acmicpc.net/problem/14888
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

op = list(map(int, input().split()))

max_val, min_val = -sys.maxsize, sys.maxsize

def backtracking(level, val):
    global max_val, min_val

    if level == n:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return


    if op[0]:
        op[0] -= 1
        backtracking(level + 1, val + nums[level])
        op[0] += 1

    if op[1]:
        op[1] -= 1
        backtracking(level + 1, val - nums[level])
        op[1] += 1

    if op[2]:
        op[2] -= 1
        backtracking(level + 1, val * nums[level])
        op[2] += 1

    if op[3]:
        op[3] -= 1
        backtracking(level + 1, int(val / nums[level]))
        op[3] += 1


backtracking(1, nums[0])

print(max_val)
print(min_val)

