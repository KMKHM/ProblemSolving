edges = [[4, 11], [1, 12], [8, 3], [12, 7],
         [4, 2], [7, 11], [4, 8], [9, 6],
         [10, 11], [6, 10], [3, 5], [11, 1],
         [5, 3], [11, 9], [3, 8]]

# edges = [[2,3], [4,3], [1,1], [2,1]]

from collections import deque, Counter

n = 0

# 진출 차수
outdegree = dict()

# 진입차수
indegree = dict()

# 진입차수, 진출 차수 기록
for a, b in edges:
    # 노드의 수 기록
    n = max([n, a, b])
    if a not in outdegree:
        outdegree[a] = 1
    else:
        outdegree[a] += 1
    if b not in indegree:
        indegree[b] = 1
    else:
        indegree[b] += 1

graph = [[] for _ in range(n+1)]


for a, b in edges:
    graph[a].append(b)
"""
1. bfs를 돌면서 방문횟수가 모드 같아야 하는 어떠한 점을 돌렸을 때 다른 경우가 나온다 => 이게 임의의 정점
2. 만약 방문횟수가 모두 같다면 도넛, 막대, 8자 판단을 해야함
3. 만약 방문횟수가 모두 1인 경우라면 막대 그래프가 있다는 뜻임
4. 만약 방문횟수가 모두 2인 경우라면 도넛 또는 8자 그래프임
5. 진출차수 + 진입차수가 4 이상이면 8자 그래프 형태를 띈다.
"""


def bfs(start):
    q = deque()
    q.append(start)
    r = Counter()
    while q:
        now = q.popleft()
        if r[now] > 1:
            continue
        r[now] += 1
        for v in graph[now]:
            q.append(v)
    return r

check = [0] * (n+1)

answer = [0, 0, 0, 0]

c = 0
num = 1

for i in range(1, n+1):
    if check[i]:
        continue

    tmp = bfs(i)

    # 방문 횟수가 모두 같아야 함
    vals = tmp.values()

    if len(set(vals)) > 1:
        c = i
    else:
        if len(tmp.keys()) == 1:
            e = list(tmp.keys())[0]
            if e not in graph[e]:
                continue

        if 1 in vals:
            answer[2] += 1

        else:
            flag = True
            for k in tmp.keys():
                if indegree[k] + outdegree[k] >= 4:
                    answer[3] += 1
                    flag = False
                    break
            if flag:
                answer[1] += 1
        for k in tmp.keys():
            check[k] = 1
    print(tmp)
answer[0] = c
print(check)
print(answer)

remain = []

for i in range(1, len(check)):
    if not check[i]:
        remain.append(i)

print(graph)

print(answer)
