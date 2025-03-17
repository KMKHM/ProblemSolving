"""
로봇 조립
문제: https://www.acmicpc.net/problem/18116
"""
import sys

input = sys.stdin.readline

n = int(input())

limit = 10**6

# 부모 테이블
parent = [i for i in range(limit + 1)]

# 개수 테이블
robot = [1] * (limit + 1)

# find 연산
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# union 연산
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return

    parent[max(root_x, root_y)] = min(root_x, root_y)
    robot[min(root_x, root_y)] += robot[max(root_x, root_y)]
    robot[max(root_x, root_y)] = 0

for _ in range(n):
    op, *nums = input().split()
    if op == "I":
        union(int(nums[0]), int(nums[1]))
    else:
        tmp = find(int(nums[0]))
        print(robot[tmp])
