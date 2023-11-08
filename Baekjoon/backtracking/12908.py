"""
텔레포트
문제: https://www.acmicpc.net/problem/12908
"""
import sys

input = sys.stdin.readline

xs, sy = map(int, input().split())
xe, se = map(int, input().split())

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

teleport = []

visited = []

for _ in range(3):
    a, b, c, d = map(int, input().split())
    teleport.append([(a, b), (c, d)])




