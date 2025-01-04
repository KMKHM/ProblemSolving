"""
퇴사
문제: https://www.acmicpc.net/problem/14501
"""
import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

res = 0

def bt(day, money):
    global res

    if day == n:
        res=max(res, money)
        return

    if day + arr[day][0] <= n:
        bt(day + arr[day][0], money + arr[day][1])

    bt(day+1, money)


bt(0, 0)

print(res)