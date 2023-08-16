import sys

input = sys.stdin.readline

n, q = map(int, input().split())

nums = list(map(int, input().split()))

change = list(map(int, input().split()))

def calc(arr, num):
    val = 0

    for i in range(n):
        temp = 1
        for j in range(4):
            idx = i+j
            if idx > n-1:
                idx -= n
            if idx == num - 1:
                temp *= (-arr[idx])
            else:
                temp *= arr[idx]
        val += temp
    return val


result = []

for num in change:
    result.append(calc(nums, num))

print(*result)