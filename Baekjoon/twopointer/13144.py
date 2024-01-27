"""
List of Unique Numbers
문제: https://www.acmicpc.net/problem/13144
"""
n = int(input())

ans = n

nums = list(map(int, input().split()))

for i in range(n-1):
    start, end = i, i+1
    while end < n:
        if nums[start] == nums[end]:
            break
        else:
            end += 1
            ans += 1
print(ans)