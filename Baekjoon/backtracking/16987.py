"""
계란으로 계란치기
문제: https://www.acmicpc.net/problem/16987
"""
import sys

input = sys.stdin.readline

n = int(input())

# 계란이 1개면 그냥 프로그램 종료
if n == 1:
    print(0)
    sys.exit(0)

# 계란 입력
eggs = [list(map(int, input().split())) for _ in range(n)]

# 정답 0으로 초기화
ans = 0

# 백트래킹
def backtrackking(level):
    global ans

    # 만약 level이 n까지 도착하면 정답 갱신
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
        return

    # 현재 계란을 제외한 모든 계란이 깨져있는 경우 탐색
    check = True

    for i in range(n):
        if i != level and eggs[i][0] > 0:
            check = False
            break
    if check:
        ans = max(ans, n - 1)
        return

    # 현재 계란이 안깨진 경우 돌면서 백트래킹
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