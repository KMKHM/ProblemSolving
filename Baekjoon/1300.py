"""
K번째 수
문제: https://www.acmicpc.net/problem/1300
"""
n = int(input())

k = int(input())

nums = [i*j for i in range(1, n+1) for j in range(1, n+1)]
nums.sort()

print(nums)