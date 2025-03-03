"""
LCS 4
문제: https://www.acmicpc.net/problem/13711
"""
import sys

input = sys.stdin.readline

n = int(input())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

dic = {num: idx for idx, num in enumerate(nums1)}

print(dic)
temp = [dic[i] for i in nums2]
print(temp)
res = []
# for i in temp:


