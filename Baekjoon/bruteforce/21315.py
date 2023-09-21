"""
카드 섞기
문제: https://www.acmicpc.net/problem/21315
"""
import sys
from itertools import product

input = sys.stdin.readline

n = int(input())

# 나와야 하는 배열
res = list(map(int, input().split()))

# 가능한 k의 후보군
possible = []

tmp = 1
while 1:
    if 2 ** tmp < n:
        possible.append(tmp)
        tmp += 1
    else:
        break

# 두 개를 뽑는 경우의 수
case = list(product(possible, repeat=2))


# 카드섞기 함수
def shuffle(arr, k):
    if k == 0:
        return arr
    temp = arr[len(arr)-k:]
    return shuffle(temp, k//2) + arr[:len(arr)-k]


for i, j in case:

    nums = [m for m in range(1, n+1)]

    if shuffle(shuffle(nums, 2**i), 2**j) == res:
        print(i, j)
        sys.exit(0)