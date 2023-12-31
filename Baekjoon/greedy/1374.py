"""
강의실
문제: https://www.acmicpc.net/problem/1374
"""
import sys, heapq

input = sys.stdin.readline

n = int(input())

lecture = []

for _ in range(n):
    a, s, t = map(int, input().split())
    lecture.append([s, t])


# 먼저 시작시간을 기준으로 정렬한다.
lecture.sort()

# 우선순위 큐 선언
q = []

# 빈 강의실에 시작시간이 제일 짦은 강의의 끝나는 시간을 넣는다.
q.append(lecture[0][1])

# 강의를 하나 넣었으므로 강의실의 개수는 1부터 시작
answer = 1

# 첫 번째 강의를 제외한 나머지 강의실 진행
for i in range(1, n):
    # 만약 가장 빨리 끝나는 강의보다 진행할 강의의 시작시간이 작다면
    if lecture[i][0] < q[0]:
        # 큐에 진행할 강의의 끝나는 시간을 넣어주고
        heapq.heappush(q, lecture[i][1])
        # 강의실의 개수 1개 더 늘려준다.
        answer += 1
    else:
        # 진행할 강의의 시작시간이 큐의 가장 빨리 끝나는 시간보다 크거나 같다면 가장 빨리 끝나는 강의 없애주고
        heapq.heappop(q)
        # 진행할 강의의 끝나는 시간을 넣어준다.
        heapq.heappush(q, lecture[i][1])

# 정답 출력
print(answer)