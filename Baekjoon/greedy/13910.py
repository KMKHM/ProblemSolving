"""
개업
문제: https://www.acmicpc.net/problem/13910
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

# dp 테이블
dp = [[0]*(n+1) for _ in range(m+1)]







