"""
치킨치킨치킨
문제: https://www.acmicpc.net/problem/16439
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

res=0

nums = [list(map(int, input().split())) for _ in range(n)]

tmp=[]
res=0
def bt(level):
    global res

    if level == 3:
        val = 0
        for num in nums:
            a = 0
            for idx in tmp:
                a = max(num[idx], a)
            val+=a
        res=max(res, val)
        return

    for i in range(m):
        if i not in tmp:
            tmp.append(i)
            bt(level+1)
            tmp.pop()
bt(0)
print(res)