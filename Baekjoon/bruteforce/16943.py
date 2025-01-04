"""
숫자 재배치
https://www.acmicpc.net/problem/16943
"""
a, b = map(int, input().split())

candidate = list(str(a))

n = len(candidate)

res = 0

check = [0] * n

def bt(level, cur):

    global res

    if level == n:
        if int(cur) < b and not cur.startswith('0'):
            res = max(int(cur), res)
        return

    for i in range(n):
        if not check[i]:
            check[i] = 1
            bt(level + 1, cur + candidate[i])
            check[i] = 0

bt(0, "")

print(res if res else -1)