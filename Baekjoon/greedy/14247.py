"""
나무 자르기
문제: https://www.acmicpc.net/problem/14247
"""
import sys

input = sys.stdin.readline

n=int(input())

tree=list(map(int, input().split()))
grow=list(map(int, input().split()))

res=0

day=n

prefix = [[0] * n for i in range(n)]

for i in range(n):
    prefix[i][0]=tree[i] + grow[i]

for i in range(n):
    for j in range(1, n):
        prefix[i][j] = prefix[i][j-1] + grow[i]

# idx=0
#
# for i in range(n):
#     temp=0
#     temp_idx=0
#     if temp:

for i in range(n):
    tree[i] += grow[i] * n

print(tree)


print(res)