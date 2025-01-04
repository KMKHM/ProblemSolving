"""
우리집엔 도서관이 있어
문제: https://www.acmicpc.net/problem/2872
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for i in range(n)]

print(list(enumerate(nums)))