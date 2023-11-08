"""
소가 정보섬에 올라온 이유
문제: https://www.acmicpc.net/problem/17128
"""
import sys

input = sys.stdin.readline

n, q = map(int, input().split())

nums = list(map(int, input().split()))

nums = nums + nums[:3]

joke = list(map(int, input().split()))

quality = []

for i in range(n):
    quality.append(nums[i]*nums[i+1]*nums[i+2]*nums[i+3])


val = sum(quality)

# 바뀌면 자신의 인덱스가 포함된 모든 합 바꿔줘야함

for a in joke:
    a -= 1
    for idx in range(a-3, a+1):
        quality[idx] *= -1
        val += 2 * quality[idx]
    print(val)

