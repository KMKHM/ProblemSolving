"""
게임
문제: https://www.acmicpc.net/problem/1072
"""
import sys, math

x, y = map(int, input().split())

if x == y:
    print(-1)
    sys.exit(0)

def get_z(x, y):
    return math.floor(y/x * 100)

z = get_z(x, y)

start = x + 1
end = 1_000_000_000
ans = 0

while start <= end:
    mid = (start + end) // 2

    if get_z(x + mid, y + mid) < z:
        start = mid + 1
    else:
        end = mid -1
        ans = mid

print(ans-x)


