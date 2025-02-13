import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

edges = []

for i in range(n):
    for j in range(n):
        if i < j:
            edges.append([i, j, board[i][j]])

parent = [i for i in range(n)]

def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    parent[max(a, b)] = min(a, b)
    return True


edges.sort(key=lambda x: x[2])

res = cnt = 0

for a, b, c in edges:
    if union(a, b):
        res += c
        cnt += 1
        if cnt == n-1:
            break

print(res)