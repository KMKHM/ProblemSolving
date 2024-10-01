"""
싸이버개강총회
문제: https://www.acmicpc.net/problem/19583
"""
import sys
from collections import defaultdict

input = sys.stdin.readline
def transform(s):
    s = s.split(":")
    return int(s[0]) * 60 + int(s[1])

dic = defaultdict(list)

start, end1, end2 = input().split()

start, end1, end2 = transform(start), transform(end1), transform(end2)

while 1:
    try:
        time, person = input().split()
        time = transform(time)
        dic[person].append(time)
    except:
        break

res = 0

for v in dic.keys():
    if len(dic[v]) == 1:
       continue
    else:
        a, b = dic[v][0], dic[v][-1]
        if a <= start:
            for t in dic[v][1:]:
                if end1 <= t <= end2:
                    res += 1
                    break

print(res)