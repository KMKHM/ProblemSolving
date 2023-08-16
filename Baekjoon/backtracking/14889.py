"""
스타트와 링크
문제: https://www.acmicpc.net/problem/14889
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]


check = [False] * n

diff = sys.maxsize


def backtracking(level, idx):

    global diff

    if level == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if check[i] and check[j]:
                    start += nums[i][j]
                elif not check[i] and not check[j]:
                    link += nums[i][j]

        diff = min(diff, abs(start - link))

    for i in range(idx, n):
        if not check[i]:
            check[i] = True
            backtracking(level + 1, i + 1)
            check[i] = False


backtracking(0, 0)
print(diff)



