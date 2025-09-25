"""
캐슬 디펜스
문제: https://www.acmicpc.net/problem/17135
"""
import sys

input = sys.stdin.readline

n, m, d = map(int, input().split())

# 궁수 3명
# 거리가 d이하인 적중에서 가장 왼쪽에 있는 적을 공격
# 같은 적이 여러 번 공격 당할 수 있음
# 공격받은 적은 게임에서 제외
# 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다.

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))



ans = 0

def bt():
    return

print(ans)