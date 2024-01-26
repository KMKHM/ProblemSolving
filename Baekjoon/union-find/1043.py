"""
거짓말
문제: https://www.acmicpc.net/problem/1043
"""
import sys

input = sys.stdin.readline

# 사람 수, 파티 수
n, m = map(int, input().split())

# 부모 테이블
parent = [i for i in range(n+1)]

# 진실을 아는 사람의 수
nums = list(map(int, input().split()))

# find
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    parent[max(a, b)] = min(a, b)


if nums[0] != 0:
    for i in nums[1:]:
        union(0, i)
else:
    print(m)
    sys.exit(0)

ans = 0
res = []
for _ in range(m):
    nums2 = list(map(int, input().split()))
    res.append(nums2)

    for k in nums2[1:]:
        if find(k) == 0:
            for q in nums2[1:]:
                union(0, q)

for i in res:
    a = len(i[1:])
    cnt = 0

    for k in i[1:]:
        if find(k) == k:
            cnt += 1

    if cnt == a:
        ans += 1
print(parent)
print(ans)




