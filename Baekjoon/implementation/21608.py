"""
상어 초등학교
문제: https://www.acmicpc.net/problem/21608
"""
import sys

input = sys.stdin.readline

n = int(input())

board = [[0] * n for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

def sit(student, nums):

    like = []

    for i in range(n):
        for j in range(n):
            weight, tmp = 0, 0
            if board[i][j]:
                continue
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if not (0<=nx<n and 0<=ny<n):
                    continue
                if board[nx][ny] in nums:
                    weight += 1
                elif not board[nx][ny]:
                    tmp += 1
            like.append([weight, tmp, [i, j]])

    like.sort(key=lambda x: (-x[0], -x[1], x[2][0], x[2][1]))
    for a, b, p in like:
        if not board[p[0]][p[1]]:
            board[p[0]][p[1]] = student
            break



dic = dict()

for _ in range(n**2):
    num = list(map(int, input().split()))
    student, nums = num[0], num[1:]
    dic[student] = nums

    sit(student, nums)

ans = 0

p = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

for i in range(n):
    for j in range(n):
        w = 0
        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if board[nx][ny] in dic[board[i][j]]:
                w += 1
        ans += p[w]

print(ans)