"""
좋은 수열
문제: https://www.acmicpc.net/problem/2661
"""
import sys

n = int(input())

nums = ["1", "2", "3"]

ans = "1"

def check(string, next_):
    next_string = (string + next_)[::-1]
    length = len(next_string)
    for i in range(1, length):
        if i + i > length:
            break
        if next_string[0:i] == next_string[i:i+i]:
            return False
    return True


def bt(cnt, answer):
    if cnt == n:
        print(answer)
        sys.exit(0)
    for num in nums:
        if check(answer, num):
            bt(cnt + 1, answer + num)

bt(1, "1")