"""
집합의 표현
문제: https://www.acmicpc.net/problem/1717
"""
import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속합 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

# 부모 테이블 초기화
parent = [0] * (v+1)

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    o, a, b = map(int, input().split())
    if o == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent,b):
            print("YES")
        else:
            print("NO")


