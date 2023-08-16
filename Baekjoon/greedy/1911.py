"""
흙길 보수하기
문제: https://www.acmicpc.net/problem/1911
"""
import sys

input = sys.stdin.readline

n, L = map(int, input().split())

road = []

for _ in range(n):
    a, b = map(int, input().split())
    road.append([a, b])

road.sort()

answer = (road[0][1] - road[0][0]) % L
tmp = road[0][1]


