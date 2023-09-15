"""
왕복
문제: https://www.acmicpc.net/problem/18311
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))

distance = [0] * (n*2)
distance[0] = nums[0]

for i in range(1, n):
    distance[i] = distance[i-1] + nums[i]


for i in range(n, 2*n):
    distance[i] = distance[i-1] + nums[2*n-i-1]

if k > sum(nums):
    tmp = n
    for i in range(n, 2*n):
        if k > distance[i]:
            tmp -= 1
            continue
        print(tmp)
        sys.exit(0)
else:
    tmp = 1
    for i in range(n):
        if k > distance[i]:
            tmp += 1
            continue
        print(tmp)
        sys.exit(0)



