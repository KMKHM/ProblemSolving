"""
배열 탈출
문제: https://www.acmicpc.net/problem/11909
"""
import sys, heapq

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

distance = [[0]*n for _ in range(n)]

dx, dy = (1, 0), (0, 1)


def dijkstra(x, y):

    q = [(x, y, 0)]

    distance[x][y] = 0

    while q:
        now_x, now_y, cnt = heapq.heappop(q)
        if distance[now_x][now_y] < cnt:
            continue
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if not (0<=nx<n) and not (0<=ny<n):
                continue
            if board[nx][ny] >= board[now_x][now_y]:
                diff = board[nx][ny] - board[now_x][now_y] + 1
                distance[nx][ny] = cnt + diff
                heapq.heappush(q, (nx, ny, distance[nx][ny]))
            heapq.heappush(q, (nx, ny, cnt))
dijkstra(0, 0)



