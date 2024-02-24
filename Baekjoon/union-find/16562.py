"""
친구비
문제: https://www.acmicpc.net/problem/16562
"""
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

nums = [0] + list(map(int, input().split()))

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(a, b):
    a, b = find(a), find(b)

    if nums[a] <= nums[b]:
        parent[b] = a
    elif nums[b] < nums[a]:
        parent[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n+1):
    p = parent[find(i)]
    if parent[i] != p:
        parent[i] = p


ans = 0

for t in set(parent):
    ans += nums[t]


print(ans if ans <= k else "Oh no")