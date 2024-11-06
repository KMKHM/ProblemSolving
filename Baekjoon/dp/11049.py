"""
행렬 곱셈 순서
문제: https://www.acmicpc.net/problem/11049
"""
import sys

input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * n

