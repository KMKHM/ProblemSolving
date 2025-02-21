"""
사다리 타기
문제: https://www.acmicpc.net/problem/2469
"""
import sys

input = sys.stdin.readline

# k = int(input())
#
# n = int(input())
#
# res = input().rstrip()
res = "ACGBEDJFIH"
origin = sorted(res)
print(origin)
board = [[1]*10 for _ in range(5)]

s = ["**-***-****", "*-*-*******", "***-*-***-*", "*-**-***-**", "***-*-*-*-*"]

for i in s:
    print(*i)

