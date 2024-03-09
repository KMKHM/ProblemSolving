"""
암호
문제: https://www.acmicpc.net/problem/1394
"""
import sys

s1 = input().rstrip()

s2 = input().rstrip()

n, m = len(s1), len(s2)

if n == 1:
    print(1)
    sys.exit(0)

# 완성하는 문자의 자리수 이전 까지는 무조건 탐색
ans = n ** (m - 1)

for i in range(m):
    # 찾으려는 문자의 인덱스
    tmp1 = s1.index(s2[i])
    tmp2 = n ** (m-i-1)
    ans += tmp1 * tmp2
    ans %= 900518

print((ans + 1) % 900518)
