"""
이모티콘
문제: https://www.acmicpc.net/problem/14226
"""
import sys

n = int(input())

# 만약 2의 제곱수이면 => 제곱수 + 1 만큼 시간이 들고
# 만약 특정 제곱수보다 사이에 있는 수면 그 더 작은 제곱수 직전 제곱수 계속 더해주면 된다?

limit = [2**x for x in range(11)]



if n in limit:
    tmp = 2
    for num in limit[1:]:
        if n == num:
            print(tmp)
            sys.exit(0)
        tmp += 2
ans = 2
t = 2
if n % 2 == 1:
    n -= 1
    ans += 1
    ans += 1
    while 1:
        t += 2
        ans += 1
        if t == n:
            break

else:
    ans += 1
    while 1:
        t += 2
        ans += 1
        if t == n:
            break
print(ans)