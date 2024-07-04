import sys, copy
from collections import deque, Counter
from itertools import combinations

input = sys.stdin.readline

n, m, k = map(int, input().split())

sec = [0] + list(map(int, input().split()))

indegree = [0] * (n+1)
outdegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    outdegree[a] += 1

start, end = 1, 0

for i in range(1, n+1):
    if outdegree[i] == 0:
        end = i
        break

def topological_sort(nums, indegree, sec):
    q = deque()
    q.append(start)

    ans = 0

    for num in nums:
        sec[num] = 0
    res = [0]
    while q:
        cur = q.popleft()
        res.append(cur)
        for v in graph[cur]:
            indegree[v] -= 1
            if not indegree[v]:
                q.append(v)

    check = [0] * (n+1)
    check[res[0]] = 1
    for i in range(1, n+1):
        val = 0
        for j in graph[i]:
            if not check[j]:
                val = max(val, sec[j])
                check[j] = 1
        ans += val
    return ans + sec[start]

answer = sys.maxsize

if k:
    for nums in list(combinations([i for i in range(2, n+1) if i != end], k)):
        answer = min(answer, topological_sort(nums, copy.copy(indegree), copy.copy(sec)))
else:
    answer = topological_sort([], indegree, sec)

print(answer)