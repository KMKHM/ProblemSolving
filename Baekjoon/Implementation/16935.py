"""
배열 돌리 3
문제: https://www.acmicpc.net/problem/16935
"""
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

nums = [list(map(int, input().split())) for _ in range(n)]

op = list(map(int, input().split()))

# 상하반전
def one(arr):
    return arr[::-1]

# 좌우반전
def two(arr):
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    return arr

# 오른쪽 90도
def three(arr):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = arr[n-1-j][i]
    return temp

def four(arr):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = arr[j][m-1-i]
    return temp

def five(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            temp[i][j+m//2]=arr[i][j]
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i+n//2][j]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i][j-m//2]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i-n//2][j]=arr[i][j]
    return temp
def siz(arr):
    temp=[[0]*m for _ in range(n)]
    for i in range(n//2):
        for j in range(m//2):
            temp[i+n//2][j]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i][j+m//2]=arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i-n//2][j]=arr[i][j]
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i][j-m//2]=arr[i][j]
    return temp

for o in op:
    if o == 1:
        nums = one(nums)
    if o == 2:
        nums = two(nums)
    if o == 3:
        nums = three(nums)
        n, m = m, n
    if o == 4:
        nums = four(nums)
        n, m = m, n
    if o == 5:
        nums = five(nums)
    if o == 6:
        nums = siz(nums)


for i in range(len(nums)):
    print(*nums[i])