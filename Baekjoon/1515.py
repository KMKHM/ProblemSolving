"""
수 이어쓰기
문제: https://www.acmicpc.net/problem/1515
"""
s = input().rstrip()

cur=0

for c in s:
    print(cur)
    if c=="0":
        if cur == 0:
            cur = 10
        else:
            cur = (cur // 10 + 1) * 10
    elif c == "9":
        cur = 9 if cur < 9 else (cur // 10 + 1) * 10 + 9
    else:
        continue