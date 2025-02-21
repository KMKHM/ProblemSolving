"""
내 선물을 받아줘 2
문제: https://www.acmicpc.net/problem/15886
"""
import sys

input = sys.stdin.readline

n = int(input())

s = input().rstrip()

print(s.count("EW"))



