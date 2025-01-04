"""
이진 검색 트리
문제: https://www.acmicpc.net/problem/5639
"""
import sys
from collections import Counter

input = sys.stdin.readline

nums = []

while True:
    try:
        nums.append(int(input()))

    except:
        break


root = nums[0]

graph = Counter()

for i in range(len(nums)):
    graph[nums[i]] = [0, 0]


for i in range(1, len(nums)):
    if nums[i] < root:
        graph[root][0]=nums[i]
        root = nums[i]