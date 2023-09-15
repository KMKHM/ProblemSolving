"""
강의실 배정
문제: https://www.acmicpc.net/problem/11000
"""
import sys

input = sys.stdin.readline

n = int(input())

lecture = []

# 입력
for _ in range(n):
    lecture.append(list(map(int, input().split())))
# ------- ------------------------------------------

# 정렬 => 끝나는 시간기준으로 먼저 정렬해야 함
# why? 시작과 동시에 끝나는 회의를 무조건 포함해야 회의를 더 할 수 있다.
lecture.sort(key=lambda x: (x[1], x[0]))
# 끝나는 시간으로 정렬 후 시작시간으로 정렬

# 무조건 1개 진행
answer = 1

# 첫 번째 회의가 끝나는 시간 => 무조건 빨리 끝나는 시간에 시작해야 회의를 많이 진행
end_time = lecture[0][1]
# 4 => 7 => 11 => 14
for i in range(1, n):
    s, e = lecture[i][0], lecture[i][1]
    if s >= end_time:
        answer += 1
        end_time = e

print(answer, end_time)


