"""
이중 우선순위 큗
문제: https://www.acmicpc.net/problem/7662
"""
import sys, heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    max_q = []
    min_q = []
    visited = [0] * n
    for i in range(n):
        op, num = input().split()
        num = int(num)
        if op == "I":
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))
            visited[i] = 1
        else:
            if num == 1: # 최대값 삭제
                # 앞에 연산중 제거된 값이 있다면 먼저 제거해줘야 함
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)

                if max_q:
                    visited[max_q[0][1]] = 0
                    heapq.heappop(max_q)
            # 최소값 삭제
            else:
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)

                if min_q:
                    visited[min_q[0][1]] = 0
                    heapq.heappop(min_q)
    if 1 not in visited:
        print("EMPTY")










