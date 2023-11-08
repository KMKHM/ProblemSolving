"""
좋은 수열
문제: https://www.acmicpc.net/problem/2661
"""
import sys

n = int(input())

nums = ["1", "2", "3"]

ans = "1"

def check(string):
    length = len(string)
    for i in range(length-1):
        for j in range(1, length//2 + 1):
            if string[i:i+j] == string[i+j:i+2*j]:
                return False
    return True


def bt(cnt, answer):
    if not check(answer):
        return

    if cnt == n:
        print(answer)
        sys.exit(0)
    for num in nums:
        bt(cnt + 1, answer + num)

bt(1, "1")