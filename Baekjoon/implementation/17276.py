"""
배열 돌리기
문제: https://www.acmicpc.net/problem/17276
"""
import sys

input = sys.stdin.readline

t = int(input())

def rotate(nums, r):
    # 주 대각선
    temp1 = [nums[i][j] for i in range(len(nums)) for j in range(len(nums)) if i == j]
    # 중간 행
    temp2 = [nums[len(nums)//2][j] for j in range(len(nums))]
    # 중간 열
    temp3 = [nums[i][len(nums)//2] for i in range(len(nums))]
    # 부 대각각선
    temp4 = [nums[i][j] for i in range(len(nums)) for j in range(len(nums)) if i+j == len(nums)-1]

    if r == 1:
        p1, p2, p3, p4 = 0, len(nums)-1, 0, 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: # 주대각선에 중간행대입
                    nums[i][j] = temp2[p1]
                    p1 += 1
                if i == len(nums)//2: # 중간행에 부대각선 대입
                    nums[i][j] = temp4[p2]
                    p2 -= 1
                if j == len(nums)//2: # 중간열에 주대각선 대입
                    nums[i][j] = temp1[p3]
                    p3 += 1
                if i + j == len(nums)-1:
                    nums[i][j] = temp3[p4]
                    p4 += 1
    else:
        p1, p2, p3, p4 = 0, 0, 0, len(nums)-1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    nums[i][j] = temp3[p1]
                    p1 += 1
                if i == len(nums)//2:
                    nums[i][j] = temp1[p2]
                    p2 += 1

                if j == len(nums)//2:
                    nums[i][j] = temp4[p3]
                    p3 += 1
                if i + j == len(nums) - 1:
                    nums[i][j] = temp2[p4]
                    p4 -= 1
    return nums



for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    a = abs(d) // 45
    if d > 0:
        for _ in range(a):
            arr = rotate(arr, 1)
    else:
        for _ in range(a):
            arr = rotate(arr, 2)

    for i in range(n):
        print(*arr[i])
