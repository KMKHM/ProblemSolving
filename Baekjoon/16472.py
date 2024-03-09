"""
고냥이
문제: https://www.acmicpc.net/problem/16472
"""
n = int(input())

s = input().rstrip()

length = len(s)

start, end = 0, 1

dic = {s[start]: 1}

# 정답
ans = 0

while start < length and end < length:
    if s[end] not in dic:
        dic[s[end]] = 1
    else:
        dic[s[end]] += 1

    if len(dic) <= n:
        end += 1
        val = sum(dic.values())
        ans = max(val, ans)
    elif len(dic) > n:
        start += 1
        end = start + 1
        dic = {s[start]: 1}

print(ans)
