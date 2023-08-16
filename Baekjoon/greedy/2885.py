"""
초콜릿 식사
문제: https://www.acmicpc.net/problem/2885
"""
import sys

k = int(input())

chocolate = 1


while chocolate <= k:
    if k == chocolate:
        chocolate = k
        print(k, 0)
        sys.exit(0)
    else:
        chocolate *= 2

action, cnt = 0, 0

action = 0

l, r = 0, chocolate

while l <= r:
    mid = (l+r)//2
    action += 1
    if mid == k:
        break
    elif mid < k:
        l = mid
    else:
        r = mid




print(chocolate, action)