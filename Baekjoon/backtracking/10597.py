"""
순열장난
문제: https://www.acmicpc.net/problem/10597
"""
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

s = input().rstrip()

length = len(s)

dic = dict(zip([i for i in range(1, 10)], [i for i in range(1, 10)]))

for a in range(10, 51):
    dic[a] = dic[a-1] + 2

target = 0

for i, j in dic.items():
    if j == length:
        target = i

nums = []

target_sum = target * (target + 1) // 2

def backtracking(char, idx):

    if idx == length:
        if target in nums:
            if sum(nums) == target_sum:
                print(*nums)
                sys.exit(0)
        return

    if idx > length-1:
        return

    if int(s[idx]) not in nums and int(s[idx]) != 0:
        nums.append(int(s[idx]))
        backtracking(char[idx+1:], idx+1)
        nums.pop()

    if int(s[idx:idx+2]) <= target:
        nums.append(int(s[idx:idx+2]))
        backtracking(char[idx+2:], idx+2)
        nums.pop()

backtracking(s, 0)