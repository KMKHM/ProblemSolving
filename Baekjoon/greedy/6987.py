"""
월드컵
문제: https://www.acmicpc.net/problem/6987
"""
import sys

input = sys.stdin.readline

ans = []

for _ in range(4):
    cup = []

    nation = list(map(int, input().split()))

    # 총합
    sum_val = 0

    # 승리, 무승부, 패배
    v, d, f = 0, 0, 0
    # 무승부한 국가수
    dn = 0
    for i in range(0, len(nation), 3):
        tmp = nation[i:i+3]
        v += tmp[0]
        d += tmp[1]
        f += tmp[2]
        if tmp[1] != 0:
            dn += 1
        cup.append(tmp)
        sum_val += sum(tmp)


    if sum_val != 30:
        ans.append(0)
    elif v != f:
        ans.append(0)
    elif d % 2 != 0 or dn % 2 == 1:
        ans.append(0)
    else:
        ans.append(1)

print(*ans)


