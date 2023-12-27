"""
타임머신
문제: https://www.acmicpc.net/problem/11657
"""
import sys

input = sys.stdin.readline

# 도시의 수, 노선의 수
n, m = map(int, input().split())

# 각 노선
edges = []

# 노선 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

# 거리
dist = [sys.maxsize] * (n+1)

# 1번도시에서 1번도시까지 거리는 0으로 초기화
dist[1] = 0

flag = False

for i in range(n):
    for s, e, w in edges:
        if dist[s] != sys.maxsize:
            temp_distance = dist[s] + w
            if temp_distance < dist[e]:
                if i == n-1:
                    flag = True
                dist[e] = temp_distance

if flag:
    print(-1)
else:
    for d in dist[2:]:
        if d == sys.maxsize:
            print(-1)
        else:
            print(d)