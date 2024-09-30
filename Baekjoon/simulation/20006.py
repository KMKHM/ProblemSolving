"""
랭킹전 대기열
문제: https://www.acmicpc.net/problem/20006
"""
import sys
from collections import OrderedDict

input = sys.stdin.readline

p, m = map(int, input().split())

room = OrderedDict()

for _ in range(p):
    level, name = input().split()
    level = int(level)

    flag = False
    for i in range(level-10, level+11):
        if i in room and len(room[i]) < m:
            room[i].append([level, name])
            flag = True
            break

    if not flag:
        room[level] = list()
        room[level].append([level, name])

print(room)

for k, v in room.items():
    if len(v) == m:
        print("Started!")
        v.sort(key=lambda x: x[1])
        for i in v:
            print(i[0], i[1])
    else:
        print("Waiting!")
        v.sort(key=lambda x: x[1])
        for i in v:
            print(i[0], i[1])