"""
단절점과 단절선
문제: https://www.acmicpc.net/problem/14675
"""
import sys

input = sys.stdin.readline

# 단절점 = 해당 정점을 제거했을 때 그 정점이 포한된 그래프가 2개이상으로 나누어짐
# 단절선 = 해당 간선을 제거했을 때 그 간선이 포함된 그래프가 2개이상으로 나누어짐

# 트리의 정점의 수
n = int(input())

indegree = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())

    indegree[a] += 1
    indegree[b] += 1


q = int(input())

for _ in range(q):
    t, k = map(int, input().split())

    if t == 1:
        # 어떤 정점을 잡았을 때 자식노드가 2개 이상이면 단절점으로 볼 수 있움
        if indegree[k] >= 2:
            print("yes")
        else:
            print("no")
    # 트리에서 모든 간선은 어차피 단절선이다.
    else:
        print("yes")
