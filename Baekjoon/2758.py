"""
로또
문제: https://www.acmicpc.net/problem/2758
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    # 1 ~ m 까지 중 n개

    res = []
    cnt = 0

    def bt(level):
        global cnt
        if level == n:
            cnt += 1
            return

        for i in range(1, m+1):
            if res:
                if res[-1] * 2 <= i and i not in res:
                    res.append(i)
                    bt(level + 1)
                    res.pop()
            else:
                res.append(i)
                bt(level+1)
                res.pop()
    bt(0)
    print(cnt)
