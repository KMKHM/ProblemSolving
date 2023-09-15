"""
문제 추천 시스템 Version 1
문제: https://www.acmicpc.net/problem/21939
"""
import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

problems = []
dic = defaultdict(set)
for _ in range(n):
    num, p = map(int, input().split())
    dic[p].add(num)

m = int(input())

for _ in range(m):
    command = list(input().split())
    if len(command) == 3:
        dic[int(command[2])].add(int(command[1]))

    else:
        if command[0] == "recommand":
            if command[1] == "1":
                tmp = list(dic.keys())[-1]
                print(dic[tmp][-1])
            else:
                tmp = list(dic.keys())[0]
                print(dic[tmp][0])


