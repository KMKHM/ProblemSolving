"""
소-난다!
문제: https://www.acmicpc.net/problem/19699
"""
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())

cows = list(map(int, input().split()))

check = [0]*n

res, result = [], set()

prime = [1] * 9001
prime[0] = prime[1] = 0

for i in range(2, int(9001**0.5)+1):
    if prime[i]:
        for j in range(i+i, 9001, i):
            prime[j] = 0


def backtracking(L):
    if len(res) == m:
        if prime[sum(res)]:
            result.add(sum(res))
        return

    for i in range(L, n):
        if not check[i]:
            check[i] = 1
            res.append(cows[i])
            backtracking(i+1)
            check[i] = 0
            res.pop()


backtracking(0)
if result:
    result = sorted(result)
    print(*result)
else:
    print(-1)
