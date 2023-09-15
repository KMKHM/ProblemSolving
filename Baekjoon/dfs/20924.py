"""
트리의 기둥과 가지
문제: https://www.acmicpc.net/problem/20924
"""
import sys

input = sys.stdin.readline

n, r = map(int, input().split())

if n == 1:
    print(0, 0)
    sys.exit(0)

indegree = [0] * (n+1)

tree = [[] for _ in range(n+1)]


for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    indegree[a] += 1

max_leaf = max(indegree)

if max_leaf == 1:
    ans = 0
    print(tree)
    for e in tree[1:]:
        if not e:
            continue
        a = e[0][1]
        ans += a
    print(ans, 0)
else:
    ans, ans1 = 0, 0
    while 1:
        if indegree[r] > 1:
            break
        ans += tree[r][0][1]
        r = tree[r][0][0]
    visited = [0] * (n+1)
    def dfs(start, score):
        global ans1
        visited[start] = 1
        if not tree[start]:
            ans1 = max(ans1, score)
        for i in tree[start]:
            dfs(i[0], score + i[1])
    dfs(r, 0)
    print(ans, ans1)


