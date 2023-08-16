import sys

input = sys.stdin.readline

n = int(input())

# 부모 테이블
parent = [i for i in range(n+1)]

# 거리 계산
def cal(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

# find 함수
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

# union 함수
def union(a, b):
    root_a, root_b = find(a), find(b)

    if root_a == root_b:
        return

    if root_a < root_b:
        parent[root_b] = parent[root_a]
    else:
        parent[root_a] = parent[root_b]


point = []

for _ in range(n):
    a, b = map(float, input().split())
    point.append((a, b))

edge = []

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        edge.append((cal(point[i][0], point[i][1], point[j][0], point[j][1]), i+1, j+1))

edge.sort()

answer = 0

for c, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)

