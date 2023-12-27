"""
팩토리얼 0의 개수
문제: https://www.acmicpc.net/problem/11687
"""
m = int(input())

left, right = 1, m*5

def zero(n):
    cnt = 0
    while n >= 5:
        cnt += (n // 5)
        n //= 5
    return cnt

res = 0

while left <= right:
    mid = (left + right) // 2
    tmp = zero(mid)

    if tmp < m:
        left = mid + 1
    else:
        right = mid - 1
        res = mid

print(res if zero(res) == m else -1)