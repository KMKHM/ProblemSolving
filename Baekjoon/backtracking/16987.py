"""
계란으로 계란치기
문제: https://www.acmicpc.net/problem/16987
"""
import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(0)
    sys.exit(0)

eggs = [list(map(int, input().split())) for _ in range(n)]

ans = -sys.maxsize

def backtrackking(level):
    global ans

    if level == n:
        cnt = 0
        for i, j in eggs:
            if i <= 0:
                cnt += 1
        ans = max(cnt, ans)
        return

    # 현재 계란 깨졌거나 내구도 0 되면 다른 계단 집기
    if eggs[level][0] <= 0:
        backtrackking(level + 1)
    else:
        for i in range(n):
            # 현재 계란빼고 안깨진 계란일 경우 백트랙킹
            if level != i and eggs[i][0] > 0:
                eggs[level][0] -= eggs[i][1]
                eggs[i][0] -= eggs[level][1]
                backtrackking(level + 1)
                # 원복
                eggs[level][0] += eggs[i][1]
                eggs[i][0] += eggs[level][1]

backtrackking(0)

print(ans)