"""
N과 M (9)
문제: https://www.acmicpc.net/problem/15663
"""
n, m = map(int, input().split())

nums = sorted(map(int, input().split()))

check = [0] * n
answer = set()
res = []

def dfs():

    if len(res) == m:
        answer.add(tuple(res))
        return
    for i in range(len(nums)):
        if not check[i]:
            check[i] = 1
            res.append(nums[i])
            dfs()
            check[i] = 0
            res.pop()

dfs()

for li in sorted(answer):
    print(*list(li))
