"""
빌런 호석
문제: https://www.acmicpc.net/problem/22251
"""
import sys
input = sys.stdin.readline

n, k, p, x = map(int, input().split())

# 7 segment
led = [
    "1110111", "0010010", "1011101", "1011011", "0111010",
    "1101011", "1101111", "1010010", "1111111", "1111011"
]

def diff(a, b):
    return sum([1 for i in range(7) if a[i] != b[i]])

cur = str(x).zfill(k)  # 현재 숫자를 k자리로 맞춤
res = 0

def dfs(pos, changed, value):
    global res

    if changed > p: return
    if pos == k:
        val = int("".join(value))
        if 1 <= val <= n and val != x:
            res += 1
        return

    now_digit = int(cur[pos])
    for d in range(10):
        seg_diff = diff(led[now_digit], led[d])
        value[pos] = str(d)
        dfs(pos + 1, changed + seg_diff, value)

dfs(0, 0, ['0'] * k)
print(res)