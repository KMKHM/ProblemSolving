"""
LCA
문제: https://www.acmicpc.net/problem/11437
"""
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# 노드의 수
n = int(input())

# tree
tree = [[] for _ in range(n+1)]

# 연결된 노드 입력
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 부모 리스트
parent = [0] * (n+1)

# 각 노드의 depth
d = [0] * (n+1)

# 각 노드의 depth가 계산되었는지 기록하기 위한 리스트
check = [0] * (n+1)

# 루트 노드부터 시작해 깊이를 구하는 함수
def dfs(x, depth):
    check[x] = 1
    d[x] = depth
    for child in tree[x]:
        if check[child]:
            continue

        parent[child] = x
        dfs(child, depth + 1)

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a

dfs(1, 0)

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))



