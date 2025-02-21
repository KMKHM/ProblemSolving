"""
근손실
문제: https://www.acmicpc.net/problem/18429
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))
visited = [0] * n
m = 500
ans = 0

def bt(level):

    global ans, m

    if m < 500:
        return

    if level == n:
        ans += 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            m = m + (nums[i]-k)
            bt(level+1)
            m = m - (nums[i]-k)
            visited[i] = 0

bt(0)
print(ans)
