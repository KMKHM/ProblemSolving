"""
출석체크
문제: https://www.acmicpc.net/problem/20438
"""
import sys

input = sys.stdin.readline

# 학생 수, 졸고 있는 학생 수, 출석 코드를 보낼 학생 수, 구간 수
n, k, q, m = map(int, input().split())

# 학생
student = [1] * (n+3)

# 졸고 있는 학생 번호
sleeping = [0] * (n+3)
for i in map(int, input().split()):
    sleeping[i] = 1

# 받은 번호
getting = list(map(int, input().split()))

# 출석체크
for num in getting:
    if sleeping[num]:
        continue

    for i in range(num, n+3, num):
        if sleeping[i]:
            continue
        student[i] = 0

student[2], tmp = 0, 0

for i in range(3, n+3):
    if student[i]:
        tmp +=1
    student[i] = tmp

for i in range(m):
    s, e = map(int, input().split())
    print(student[e]-student[s-1])