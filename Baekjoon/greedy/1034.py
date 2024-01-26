"""
램프
문제: https://www.acmicpc.net/problem/1034
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for i in range(n):
    a = input().rstrip()

k = int(input())