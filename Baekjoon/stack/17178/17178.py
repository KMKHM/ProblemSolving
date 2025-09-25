"""
줄서기
문제: https://www.acmicpc.net/problem/17178
"""
from collections import deque

n = int(input())

# 순서보장큐
sort_arr = []

input_arr = []

q = deque()

for _ in range(n):
    arr = list(input().split())
    sort_arr += arr
    input_arr+= arr

sorted_q = deque(sorted(sort_arr, key=lambda x: (x[0], int(x[2:]))))
wait_q = deque()

for i in range(len(input_arr)):
    # 현재 사람
    cur = input_arr[i]

    # 현재 사람이 가장 먼저 입장해야 할 사람이라면, 순서 큐에서 제거
    if cur == sorted_q[0]:
        sorted_q.popleft()
        while wait_q and sorted_q:
            if wait_q[0] == sorted_q[0]:
                wait_q.popleft()
                sorted_q.popleft()
            else:
                break
    else:
        wait_q.appendleft(cur)

print("GOOD" if not wait_q else "BAD")