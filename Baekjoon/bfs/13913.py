"""
숨바꼭질 4
문제: https://www.acmicpc.net/problem/13913
"""
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

check = [-1] * (100000 + 1)
path = []

def bfs(start):
    q = deque()
    q.append(start)
    check[start] = 0

    while q:
        cur = q.popleft()
        if cur == k:
            print(check[k])
            print(path)
            tmp = cur
            while tmp != start:
                print(tmp)
                path.append(tmp)
                tmp = check[tmp]
            path.append(start)
            print(path[::-1])
            break

        for nx in [cur-1, cur+1, cur * 2]:
            if 0 <= nx < 100001 and check[nx] == -1:
                check[nx] = check[cur] + 1
                q.append(nx)
bfs(n)