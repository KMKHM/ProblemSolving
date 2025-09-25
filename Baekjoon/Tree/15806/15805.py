"""
트리 나라 관광 가이드
문제: https://www.acmicpc.net/problem/15805
"""
import sys

input = sys.stdin.readline

k = int(input())

arr = list(map(int, input().split()))
n = len(set(arr))

check = [0] * n
check[arr[0]] = 1
res = [-1] * n

dic = dict()

for i in range(n):
    dic[i] = list()

for i in range(1, k):
    if check[arr[i]]:
        continue
    if check[arr[i-1]]:
        dic[arr[i-1]].append(arr[i])

    check[arr[i]] = 1

for k, v in dic.items():
    for i in v:
        res[i] = k

print(n)
print(*res)