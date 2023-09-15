"""
강의실 배정
문제: https://www.acmicpc.net/problem/11000
"""
import heapq
import sys

input = sys.stdin.readline

n = int(input())

lecture = []

# 입력
for _ in range(n):
    lecture.append(list(map(int, input().split())))

# 정렬
lecture.sort()

# 무조건 강의실 1개는 있어야 함
answer = 1

# 처음 강의가 끝나는 시간
q = [lecture[0][1]]

for i in range(1, n):
    # 시작시간, 끝나는 시간
    s, t = lecture[i][0], lecture[i][1]

    # 큐에 있는 끝나는 시간이 시작보다 늦으면 강의실 하나 추가하고 큐에 비교하고 있는 끝나는 시간 넣음
    if q[0] > s:
        heapq.heappush(q, t)
        answer += 1
    # 큐에 있는 가장 빠른 끝나는 시간이 비교 중인 시작시간과 같거나 작으면 제거해주고 끝나는 시간 넣음
    else:
        heapq.heappop(q)
        heapq.heappush(q, t)

print(answer)

