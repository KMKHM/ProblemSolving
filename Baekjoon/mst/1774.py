import sys
input = sys.stdin.readline


n, m = map(int, input().split())

parent = [i for i in range(n+1)]

v = []

edges = []

# 거리 계산
def cal(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a, root_b = find(a), find(b)
    if root_a == root_b:
        return

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


for _ in range(n):
    a, b = map(int, input().split())
    v.append((a, b))

# 통로 => 미리 union 해줌
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)



# 정답
result = 0

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((cal(v[i][0], v[i][1], v[j][0], v[j][1]), i+1, j+1))

edges.sort()

for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += c

print('%.2f' %(result))




