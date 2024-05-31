"""
A -> B
문제: https://www.acmicpc.net/problem/16953
"""
a, b = map(int, input().split())

ans = 0

while 1:
    s_b = str(b)
    if len(s_b) > 1:
        if s_b[-1] == "1":
            b = int(s_b[:len(s_b)-1])
            ans += 1
            if a == b:
                break
    elif b % 2 == 0:
        b //= 2
        ans += 1
        if a == b:
            break
    else:
        break

ans = ans + 1 if a== b else -1

print(ans)