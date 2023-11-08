"""
미술가 미미
https://www.acmicpc.net/problem/20950
"""
import sys, math

input = sys.stdin.readline

n = int(input())

rgb = [list(map(int, input().split())) for _ in range(n)]

check = [0] * n

origin = list(map(int, input().split()))

r, g, b = 0, 0, 0

diff = sys.maxsize

temp = [0]*3

def bt(level, cnt):
    global diff, r, g, b
    if cnt >= 2:
        val = [math.trunc(r / cnt), math.trunc(g / cnt), math.trunc(b / cnt)]
        diff = min(diff, abs(val[0]-origin[0]) + abs(val[1]-origin[1]) + abs(val[2]-origin[2]))



    for i in range(level, n):
        if not check[i] and cnt < 7:
            check[i] = 1
            r += rgb[i][0]
            g += rgb[i][1]
            b += rgb[i][2]
            bt(i + 1, cnt + 1)
            check[i] = 0
            r -= rgb[i][0]
            g -= rgb[i][1]
            b -= rgb[i][2]


bt(0, 0)

print(diff)