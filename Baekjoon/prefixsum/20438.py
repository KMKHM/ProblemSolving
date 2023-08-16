"""
출석체크
문제: https://www.acmicpc.net/problem/20438
"""
import sys

input = sys.stdin.readline

# 전체 학생 수, 졸고 있는 학생 수, 출석 코드를 보낼 학생 수, 주어질 구간
n, k, q, m = map(int, input().split())

# 졸고 있는 학생
sleep = list(map(int, input().split()))

# 코드를 보낼 학생들
code = list(map(int, input().split()))


# 구간합 배열
prefix_sum = [0] * (n+3)

cnt = 1

for c in code:
    for i in range(c, n+3, c):



print(prefix_sum)

for _ in range(m):
    a, b = map(int, input().split())
