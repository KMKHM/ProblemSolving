"""
수강신청
문제: https://www.acmicpc.net/problem/13414
"""
import sys

input = sys.stdin.readline

k, l = map(int, input().split())

cnt = 0

dic = dict()

for _ in range(l):
    num = input().rstrip()
    if num not in dic:
        dic[num] = 1
    else:
        del dic[num]
        dic[num] =1

for v in dic.keys():
    if cnt < k:
        cnt += 1
        print(v)
        if cnt == k:
            break