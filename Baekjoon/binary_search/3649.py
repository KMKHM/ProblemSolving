"""
로봇 프로젝트
문제: https://www.acmicpc.net/problem/3649
"""
import sys

input = sys.stdin.readline

while 1:
    try:
        x = int(input()) * 10000000
        n = int(input())
        nums = sorted([int(input()) for _ in range(n)])

        answer1, answer2 = 0, 0

        start, end = 0, n - 1

        while start < end:
            val = nums[start] + nums[end]

            if val == x:
                answer1, answer2 = nums[start], nums[end]
                break
            elif val < x:
                start += 1
            else:
                end -= 1

        if answer1 == 0 and answer2 == 0:
            print("danger")
        else:
            print("yes", answer1, answer2)
    except:
        break