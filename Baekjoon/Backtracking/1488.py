"""
연산자 끼워넣기
문제: https://www.acmicpc.net/problem/14888
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

# +, -, *, /
operation = list(map(int, input().split()))

depth = len(nums) - 1

# 정답
max_val, min_val = -sys.maxsize, sys.maxsize

def bt(level, val):
    global max_val, min_val

    if level == depth:
        max_val = max(max_val, val)
        min_val = min(min_val, val)

    # + 가 가능하면
    if operation[0]:
        operation[0] -= 1
        bt(level+1, val + nums[level+1])
        operation[0] += 1
    # - 가 가능하면
    if operation[1]:
        operation[1] -= 1
        bt(level+1, val - nums[level+1])
        operation[1] += 1
    # * 가 가능하면
    if operation[2]:
        operation[2] -= 1
        bt(level + 1, val * nums[level + 1])
        operation[2] += 1

    # / 가 가능하면
    if operation[3]:
        operation[3] -= 1
        bt(level + 1, int(val / nums[level + 1]))
        operation[3] += 1

bt(0, nums[0])

print(max_val)
print(min_val)