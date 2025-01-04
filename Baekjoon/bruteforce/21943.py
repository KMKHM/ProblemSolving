"""
연산 최대로
문제: https://www.acmicpc.net/problem/21943
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

operation = list(map(int, input().split()))

ans = -sys.maxsize
temp = [[] for _ in range(operation[1]+1)]

print(temp)
def bt(level, value):
    global ans

    if level == n-1:
        ans = max(ans, value)
        return

    if operation[0]:
        operation[0]-=1
        bt(level+1, value + nums[0])
        operation[0]+=1

    if operation[1]:
        operation[1]-=1
        bt(level+1, value * nums[level])
        operation[1]+=1

bt(0, 0)

print(ans)