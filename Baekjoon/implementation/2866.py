"""
문자열 잘라내기
문제: https://www.acmicpc.net/problem/2866
"""
import sys

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]

cnt = 0

arr = list("".join(s) for s in zip(*board))

for i in range(r):
    if len(set("".join(s) for s in zip(*board[i+1:]))) == len(arr):
        cnt += 1
    else:
        break

print(cnt)