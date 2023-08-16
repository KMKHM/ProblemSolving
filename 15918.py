"""
랭퍼든 수열쟁이야!
문제: https://www.acmicpc.net/problem/15918
"""
import sys

input = sys.stdin.readline

n, x, y = map(int, input().split())

diff = y-x-1

arr = [0] * (2*n)

arr[x-1] = arr[y-1] = diff

def backtracking(idx, num):

    answer = 0

    if 0 not in arr:
        answer += 1
        return

    for i in range(2*n):
        if arr[i]:
            continue

        arr[i] = num