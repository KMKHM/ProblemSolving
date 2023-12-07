"""
두 배 더하기
문제: https://www.acmicpc.net/problem/12931
"""
import sys

input = sys.stdin.readline

n = int(input())

b = list(map(int, input().split()))

ans = 0

while sum(b) != 0:
    for i in range(n):
        # 0이면 그냥 지나감
        if b[i] == 0:
            continue
        # 1이거나 2로 안나눠지면 1 빼줌
        elif b[i] == 1 or b[i] % 2 != 0:
            b[i] -= 1
            ans += 1
    if sum(b) == 0:
        break
    # 위의 과정을 거치면 모두 0이거나 2로 나누어지는 배열임 => 전부 2로 나눠줌
    for i in range(n):
        b[i] //= 2
    ans += 1

print(ans)

