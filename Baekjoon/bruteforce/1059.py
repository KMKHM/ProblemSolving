# """
# 좋은 구간
# 문제: https://www.acmicpc.net/problem/1059
# """
# import sys
#
# input = sys.stdin.readline
#
# L = int(input())
#
# nums = list(map(int, input().split()))
#
# n = int(input())
#
# if n in nums:
#     print(0)
#     sys.exit(0)
#
# nums.sort()
#
#
# lower, upper = 0, 0
#
#
# for i in range(L-1):
#     if nums[i] < n < nums[i+1]:
#