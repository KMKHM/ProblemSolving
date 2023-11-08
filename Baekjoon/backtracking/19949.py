"""
문제: 영재의 시험
https://www.acmicpc.net/problem/19949
"""
import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

answer = list(map(int, input().split()))

res = 0

temp = []

def bt(level):
    global res

    if level == 10:
        cnt = 0

        for i in range(10):
            if temp[i] == answer[i]:
                cnt += 1

        if cnt >= 5:
            res += 1
        return

    for i in range(1, 6):
        if level > 1 and temp[level - 2] == temp[level - 1] == i:
            continue
        temp.append(i)
        bt(level + 1)
        temp.pop()


bt(0)

print(res)