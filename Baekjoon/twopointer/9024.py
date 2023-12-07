"""
두 수의 합
문제: https://www.acmicpc.net/problem/9024
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    # 차이
    diff = sys.maxsize

    # 개수
    cnt = 1

    nums = sorted(list(map(int, input().split())))

    for i in range(n):
        left = i + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            tmp = nums[i] + nums[mid]
            val = abs(tmp-k)

            if k < tmp:
                right = mid - 1
            else:
                left = mid + 1

            if val < diff:
                cnt = 1
                diff = val
            elif val == diff:
                cnt += 1
    print(cnt)