"""
https://www.acmicpc.net/problem/4803
"""
import sys
from collections import deque


input = sys.stdin.readline

def bfs(tree, visited, start):
    queue = deque([start])
    visited[start] = True
    node_cnt = edge_cnt = 0

    while queue:
        curr_node = queue.popleft()
        node_cnt += 1

        for node in tree[curr_node]:
            edge_cnt += 1
            if not visited[node]:
                visited[node] = True
                queue.append(node)

    # 간선은 양방향으로 저장되므로 2로 나누어준다.
    edge_cnt //= 2

    # 트리 조건: 간선 수는 정점 수 - 1이어야 함
    return True if edge_cnt == node_cnt-1 else False

order = 1
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)  # 양방향 간선 저장

    visited = [False] * (n + 1)
    ret = 0

    for i in range(1, n + 1):
        if not visited[i]:
            if bfs(tree, visited, i):
                ret += 1

    print(f"Case {order}: ", end="")
    if ret == 0:
        print("No trees.")
    elif ret == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {ret} trees.")

    order += 1