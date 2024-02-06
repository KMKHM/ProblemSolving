"""
사과나무
문제: https://www.acmicpc.net/problem/19539
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
val = sum(nums)
# 물뿌리개 2개 => 1, 2 만큼 성장 동시에 사용해야
# 두 개의 나무를 (2,1), (1,2)로 빼거나 한 개의 나무를 3으로 빼야 함

if val % 3 != 0:
    print("NO")
else:
    cnt = 0

    # 여기서 1
    d = val // 3

    for i in range(n):
        cnt += (nums[i] // 2)
        print(nums[i] // 2)