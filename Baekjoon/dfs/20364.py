"""
부동산 다툼
문제: https://www.acmicpc.net/problem/20364
"""
import sys

input = sys.stdin.readline

n, q = map(int, input().split())

# 트리 선언
tree = [[] for _ in range(n+1)]

# 트리 만들기
for i in range(1, n+1):
    left, right = 2 * i, 2 * i + 1
    if 1<=left<=n:
        tree[i].append(left)
    if 1<=right<=n:
        tree[i].append(right)

# 방문
visited = [0] * (n+1)

# DFS
def dfs(start, target):
    c = 0
    if start == target:
        return

    else:
        for v in tree[start]:
            if not visited[v]:
                c = dfs(v, target)
            else:
                c = v
                break
    return c



nums = [int(input()) for _ in range(q)]
ans = []
for num in nums:
     a = dfs(1, num)
     print(a)

# for num in nums:
#     if visited[num]:
#         print(0)
#     else:
#         print()


