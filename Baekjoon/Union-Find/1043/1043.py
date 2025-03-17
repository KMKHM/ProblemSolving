"""
거짓말
문제: https://www.acmicpc.net/problem/1043
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
true = list(map(int, input().split()))  # 진실을 아는 사람 수, 번호
partys = [list(map(int, input().split())) for _ in range(m)]

def union(a, b):
    x = find(a)
    y = find(b)
    parent[max(x, y)] = min(x, y)


def find(x):
    if parent[x] == x:
        return parent[x]
    return find(parent[x])

if true[0] == 0:
    print(m)
    sys.exit(0)

for i in range(1, len(true)):   # 진실을 아는 사람 union
    union(0, true[i])

for party in partys:            # 파티마다 사람들 union
    for i in range(2, len(party)):
        union(party[1], party[i])

answer = 0


for party in partys:
    if find(party[1]) != 0:
        answer += 1

print(answer)