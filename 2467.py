"""
용액
문제: https://www.acmicpc.net/problem/2467
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

left, right = 0, n-1

# 정답 용액
a, b = 0, 0

# 정답
answer = sys.maxsize


while left < right:

    tmp = nums[left] + nums[right]

    if abs(tmp) < answer:
        answer = abs(tmp)
        a, b = nums[left], nums[right]
        if answer == 0:
            print(a, b)
            sys.exit(0)

    elif tmp < 0:
        left += 1
    else:
        right -= 1

print(a, b)
