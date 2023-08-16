"""
행성 터널
문제: https://www.acmicpc.net/problem/2887
"""
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

# 부모 테이블
parent = [i for i in range(n)]

# 비용
point = []

# 간선
edges = []

# find
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# union
def union(a, b):
    root_a, root_b = find(a), find(b)
    parent[max(root_a, root_b)] = min(root_a, root_b)

# # 거리 계산
# def calc(x1, y1, z1, x2, y2, z2):
#     return min(abs(x1-x2), abs(y1-y2), abs(z1-z2))

# 좌표 입력
for i in range(n):
    a, b, c = map(int, input().split())
    point.append((a, b, c, i))

# # edge
# for i in range(n-1):
#     for j in range(i+1, n):
#         edges.append((calc(point[i][0], point[i][1], point[i][2], point[j][0], point[j][1], point[j][2]), i, j))

# x, y, z 3개 좌표별 정렬 => 후보군을 x,y,z 별로 모아둠
for i in range(3):
    point.sort(key=lambda x: x[i])
    for j in range(1, n):
        edges.append((abs(point[j - 1][i] - point[j][i]), point[j - 1][3], point[j][3]))

# 비용 기준으로 정렬
edges.sort()

print(edges)

# 정답
ans = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost

print(ans)

