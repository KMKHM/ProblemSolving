"""
한윤정이 이탈리아에 가서 아이스크림을 사먹는데
문제: https://www.acmicpc.net/problem/2422
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(1, n+1)]

avoid = [[1] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    avoid[a][b] = avoid[b][a] = 0

res=0

for i in range(1, n-1):
    for j in range(i+1, n):
        for k in range(j+1, n+1):
            if avoid[i][k] and avoid[j][k] and avoid[i][j]:
                res+=1

print(res)