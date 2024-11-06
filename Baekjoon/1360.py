"""
되돌리기
문제: https://www.acmicpc.net/problem/1360
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

dic = Counter()
# cur = ""
dic[0] = ""

for _ in range(n):
    command, op, time = input().split()
    time = int(time)

    if command == "type":
        dic[time] = dic[sorted(dic.keys())[-1]] + op
    else:
        op = int(op)
        tmp = ""
        cur=time
        for _ in range(op):
            cur -=1
            if cur not in dic:
                continue
            tmp = dic[cur]
        if cur == 0:
            dic[time] = ""
            continue
        dic[time] = dic[sorted(i for i in dic.keys() if i < cur)[-1]]
print(dic[max(dic.keys())])