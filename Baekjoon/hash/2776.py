"""
암기왕
문제: https://www.acmicpc.net/problem/2776
"""
import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dic = sorted(map(int, input().split()))
    m = int(input())

    nums = list(map(int, input().split()))

    for num in nums:
        left, right, flag = 0, n-1, False
        while left <= right:
            mid = (left + right) // 2
            if dic[mid] == num:
                flag = True
                break
            elif dic[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        print(1 if flag else 0)
