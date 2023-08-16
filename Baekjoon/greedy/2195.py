"""
문자열 복사
문제: https://www.acmicpc.net/problem/2195
"""
s, p = input().rstrip(), input().rstrip()

start = ""
temp = ""

ans = 0

for i in range(len(p)):
    temp += p[i]

    if temp in s:
        continue

    elif temp not in s:
        m = len(temp)
        start += temp[:m-1]
        temp = temp[-1]
        ans += 1

if start != p:
    start += temp
    ans += 1

print(ans)

