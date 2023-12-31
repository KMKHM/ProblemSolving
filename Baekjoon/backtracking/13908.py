"""
비밀번호
문제: https://www.acmicpc.net/problem/13908
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(input().split())

# 정답
ans = 0
res = []
def backtracking(level):
    global ans

    if level == n:
        for num in nums:
            if num not in res:
                return
        ans += 1
        return

    for i in range(10):
        res.append(str(i))
        backtracking(level+1)
        res.pop()

backtracking(0)
print(ans)