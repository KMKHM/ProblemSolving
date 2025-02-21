"""
선발명단
문제: https://www.acmicpc.net/problem/3980
"""
import sys

input = sys.stdin.readline

c = int(input())

def bt(level):
    global ans

    if level == 11:
        ans = max(sum(temp), ans)
        return

    for i in range(11):
        if not checked[i]:
            if position[level][i]:
                checked[i] = 1
                temp.append(position[level][i])
                bt(level+1)
                temp.pop()
                checked[i] = 0

for _ in range(c):
    position = [list(map(int, input().split())) for _ in range(11)]
    # 정답
    ans = 0
    # 선수 넣을 배열
    temp = []
    # 방문 여부
    checked = [0]*12

    bt(0)
    print(ans)
