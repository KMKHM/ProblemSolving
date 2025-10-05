"""
고층 건물
문제: https://www.acmicpc.net/problem/1027
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

res = [0] * n

def cal(x1, y1, x2, y2):
    return (y2-y1) / (x2-x1)

for i in range(n-1):
    val = -sys.maxsize
    for j in range(i+1, n):
        temp = cal(i, arr[i], j, arr[j])
        if not temp <= val:
            val = max(val, temp)
            res[i]+=1; res[j]+=1

print(max(res))