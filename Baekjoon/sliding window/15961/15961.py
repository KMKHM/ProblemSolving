"""
회전 초밥
문제: https://www.acmicpc.net/problem/15961
"""
import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
count = 1
s = [0] * (d+1)
s[c] = 1
data = []
for i in range(n):
    data.append(int(input()))

for i in range(k):
    s[data[i]] += 1
    if s[data[i]] == 1:
        count += 1

answer = count

for i in range(n-1):
    s[data[i]] -= 1
    if s[data[i]] == 0:
        count -= 1
    s[data[(i+k) % n]] += 1
    if s[data[(i+k) % n]] == 1:
        count += 1
    answer = max(answer, count)

print(answer)