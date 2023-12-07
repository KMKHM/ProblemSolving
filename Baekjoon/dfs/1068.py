"""
트리
문제: https://www.acmicpc.net/problem/1068
"""
import sys

input = sys.stdin.readline

# 노드의 수
n = int(input())

# 노드
nums = list(map(int, input().split()))

# 트리
tree = [[] for _ in range(n)]

# 지울 노드
remove = int(input())

# 루트 노드
root = 0

# 각 노드의 진출 차수
outdegree = [0] * n

for i in range(n):
    # -1 이면 리프 노드
    if nums[i] == -1:
        root = i
        continue
    # 아니면 방향설정해서 붙여주기
    tree[nums[i]].append(i)
    outdegree[nums[i]] += 1

# 방문 리스트
visited = [0] * n

# 깊이우선탐색
def dfs(v):

    visited[v] = 1

    if v == remove:
        print(0)
        sys.exit(0)

    for c in tree[v]:
        # 만약 자식 노드가 지울 노드라면 진출 차수에서 1 빼줌
        if c == remove:
            outdegree[v] -= 1
            continue
        dfs(c)

# 루트 노드부터 탐색시작
dfs(root)

for i in range(n):
    # 방문하지 못한 노드라면
    if not visited[i]:
        # 진출차수는 -1로 표시
        outdegree[i] = -1
        # 방문하지 못한 노드의 자식 노드의 진출차수도 -1로 표시
        for j in tree[i]:
            outdegree[j] = -1

print(outdegree.count(0))





