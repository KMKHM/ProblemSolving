"""
홀수 홀린 호석
문제: https://www.acmicpc.net/problem/20164
"""
import sys

input = sys.stdin.readline

s = input().rstrip()

# 정답
max_val = -sys.maxsize
min_val = sys.maxsize

odds = ["1", "3", "5", "7", "9"]

# 홀수의 개수 판단
def odds_nums(string):
    res = 0
    for char in string:
        if char in odds:
            res += 1
    return res

# for i in range(1, len(s) - 1):
#     for j in range(i + 1, len(s)):
#         print(s[:i], s[i:j], s[j:])

# 재귀 함수
def recurr(string, cnt):
    global max_val, min_val

    length = len(string)

    if length == 1:
        tmp = 1 if string in odds else 0
        cnt += tmp

        max_val = max(max_val, cnt)
        min_val = min(min_val, cnt)

        return

    if length == 2:
        recurr(str(int(string[0]) + int(string[1])), cnt + odds_nums(string))


    if length >= 3:
        # 3개의 수로 분할
        tmps = odds_nums(string)
        for i in range(1, len(string)-1):
            for j in range(i+1, len(string)):
                new_string = str(int(string[:i]) + int(string[i:j]) + int(string[j:]))
                recurr(new_string, cnt + tmps)


recurr(s, 0)
print(min_val, max_val)

