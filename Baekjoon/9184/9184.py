"""
신나는 함수 실행
"""
import sys

input = sys.stdin.readline

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

def recur(a, b, c):
    if a <=0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return recur(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = recur(a, b, c-1) + recur(a, b-1, c-1) - recur(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())

    if a == b and b == c and a == -1:
        sys.exit(0)

    if all([a, b, c]) > 20:
        a = b = c = 20

    print(f"w({a}, {b}, {c}) = {recur(a, b, c)}")