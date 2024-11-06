"""
홀수 홀린 호석
문제: https://www.acmicpc.net/problem/20164
"""
import sys

s = input().rstrip()

# 정답
max_val = -sys.maxsize
min_val = sys.maxsize

odds = ["1", "3", "5", "7", "9"]

def odds_nums(string):
    res = 0
    for char in string:
        if char in odds:
            res += 1
    return res

# 재귀 함수
def recurr(string, cnt):

    global max_val, min_val

    if len(string) == 1:
        tmp = 1 if string in odds else 0
        cnt += tmp
        max_val = max(max_val, cnt)
        min_val = min(min_val, cnt)
        return

    if len(string) == 2:
        recurr(str(int(string[0]) + int(string[1])), cnt + odds_nums(string))

    if len(string) >= 3:
        tmps = odds_nums(string)
        for i in range(1, len(string)-1):
            for j in range(i+1, len(string)):
                new_string = str(int(string[:i]) + int(string[i:j]) + int(string[j:]))
                recurr(new_string, cnt + tmps)

recurr(s, 0)

print(min_val, max_val)