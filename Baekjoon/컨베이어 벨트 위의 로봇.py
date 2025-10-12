"""
https://www.acmicpc.net/problem/20055
"""
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

belt = deque(list(map(int, input().split())))

level = 0

# 로봇 큐
rq = deque([0]*n)

cnt = 0

while cnt < k:
    level += 1

    # 벨트 & 로봇 회전
    belt.rotate(1); rq.rotate(1)
    # 로봇 내림
    rq[n-1] = 0

    # 로봇 이동
    for i in range(n-2, -1, -1):
        if belt[i+1] and not rq[i+1] and rq[i]:
            rq[i] = 0
            rq[i+1] = 1
            belt[i+1] -= 1
            if not belt[i+1]:
                cnt +=1
    # 로봇 내림
    rq[n-1] = 0

    # 로보트 올리기
    if belt[0] and not rq[0]:
        belt[0] -= 1
        rq[0] = 1
        if not belt[0]:
            cnt += 1

print(level)