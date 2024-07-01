"""
블랙 프라이데이
문제: https://www.acmicpc.net/problem/18114
"""
import sys

input = sys.stdin.readline

n, c = map(int, input().split())

arr = sorted(map(int, input().split()))

if arr[0] > c:
    print(0)
    sys.exit(0)

for i in range(n-2):
    left, right = i + 1, n - 1
    while left < right:
        if arr[right] == c or arr[left] == c or arr[i] == c:
            print(1)
            sys.exit(0)
        elif arr[right] + arr[left] == c or arr[i] + arr[right] == c or arr[left] + arr[i] == c:
            print(1)
            sys.exit(0)
        elif arr[right] + arr[left] + arr[i] == c:
            print(1)
            sys.exit(0)
        elif arr[right] + arr[left] + arr[i] < c:
            left += 1
        elif arr[right] + arr[left] + arr[i] > c:
            right -= 1
        elif arr[i] > c:
            print(0)
            sys.exit(0)
print(0)

