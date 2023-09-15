"""
기적의 매매법
문제: https://www.acmicpc.net/problem/20546
"""
import sys

input = sys.stdin.readline

# 성민, 준현의 현금
n = m = int(input())

# 14일치 주식
stock = list(map(int, input().split()))

# 성민 준현
se, ju = 0, 0

# 성민
for i in range(14):
    if n >= stock[i]:
        # 주식 수
        se += (n // stock[i])
        # 현금에서 주식 수를 빼줘야 함
        n -= ((n // stock[i]) * stock[i])

# 3일 연속 상승, 3일 연속 하락
up, down = 0, 0

# 준현
for i in range(1, 13):
    # 현재 주식이 전날보다 올랐다면
    if stock[i-1] < stock[i]:
        # 상승 + 1
        up += 1
        # 하락 0으로 초기화
        down = 0
    # 떨어졌다면
    elif stock[i] < stock[i-1]:
        # 하락 + 1
        down += 1
        # 상승 초기화
        up = 0

    if down >= 3:
        if m >= stock[i]:
            # 주식 수
            ju += (m // stock[i])
            # 현금에서 주식 수를 빼줘야 함
            m -= ((m // stock[i]) * stock[i])

    # 3일 연속 상승했을 때
    elif up == 3:
        # 매매한 주식이 없다면
        if ju == 0:
            up = 0
            continue
        # 매매한 주식이 있다면 현 자산(m)에 주식 수와 주식 가격을 곱해서 더해주고 주식수 초기화
        m += ju * stock[i]
        ju = 0
        up = 0


# 현금 + 마지막날 주가 * 주식 수
a = n + stock[13] * se # 준혁
b = m + stock[13] * ju # 성민

if a < b:
    print("TIMING")
elif a > b:
    print("BNP")
else:
    print("SAMESAME")

