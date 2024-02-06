"""
순열의 순서
문제: https://www.acmicpc.net/problem/1722
"""
import sys, math

input = sys.stdin.readline

n = int(input())

case = math.factorial(n)

# 경우의 수 (n-1)! 누적으로 더함
check = [case // n]

for _ in range(n-1):
    check.append(check[-1] + check[0])


problem = list(map(int, input().split()))

condition = 0

nums = [i for i in range(1, n+1)]

# k번째 수열 출력
if problem[0] == 1:
    condition = problem[1]
    res = []
    for i in range(len(check)):
        if condition < check[i]:
           res.append(nums[i])
           break

    # def
    #
    # print(res)

else:
    condition = problem[1:]
