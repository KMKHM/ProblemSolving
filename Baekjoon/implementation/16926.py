"""
배열 돌리기 1
문제: https://www.acmicpc.net/problem/16926
"""
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]


