import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

egg = deque()

for _ in range(n):
    a, b = map(int, input().split())
    egg.append((a, b))


if n == 1:
    print(0)
    sys.exit(0)

cnt = 0

idx = 0

while idx < n and egg:
    left = egg.popleft()
    for num in egg:
        if left[0] - num[1] > 0:
            pass



