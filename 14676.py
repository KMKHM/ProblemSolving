"""
영우는 사기꾼?
문제: https://www.acmicpc.net/problem/14676
"""
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

check = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

flag = True

for _ in range(k):
    a, b = map(int, input().split())

    if a == 1:
        for prev in graph[b]:
            if not check[prev]:
                flag = True
                print("Lier!")
                sys.exit(0)
        check[b] += 1
    else:
        if not check[b]:
            print("Lier!")
            sys.exit(0)
        check[b] -= 1

print("King-God-Emperor")

"""
import sys
from collections import defaultdict

input = sys.stdin.readline

# n : 건물 종류의 개수, M : 건물 사이의 관계수, k : 영우의 게임 정보의 개수
n, m, k = map(int, input().split())

graph = defaultdict(list)  # 건물 관계
indegree = [0] * (n + 1)  # 진입 차수
build = [0] * (n + 1)  # 빌딩 몇개 지어졌는지
check = False  # 치트키 여부

for _ in range(m):  # 건물 관계
    x, y = map(int, input().split())
    graph[x].append(y)  # x를 건설해야 y를 건설 가능
    indegree[y] += 1  # 진입차수

for _ in range(k):  # 영우의 게임 정보
    t, a = map(int, input().split())
    if t == 1:  # 건설
        if indegree[a]:  # 진입 차수가 있다면 바로 건설 X
            check = True
            break
        build[a] += 1  # a 빌딩 하나 건설
        if build[a] == 1:  # a 빌딩 지어진 경우
            for i in graph[a]:  # 관련 건물들 진입 차수 1씩 감소
                indegree[i] -= 1

    else:  # 파괴
        if build[a] <= 0:  # a 빌딩이 지어진 적 없는 경우
            check = True
            break
        build[a] -= 1  # a 빌딩 하나 파괴
        if not build[a]:  # 마지막 건물이 파괴된 경우
            for i in graph[a]:  # 관련 건물들 진입 차수 1씩 증가
                indegree[i] += 1

if check:  # 치트키 사용했다면
    print('Lier!')
else:
    print('King-God-Emperor')
"""