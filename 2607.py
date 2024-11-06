"""
비슷한 단어
문제: https://www.acmicpc.net/problem/2607
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

start = input().rstrip()

s = [input().rstrip() for _ in range(n-1)]

ans=0

for w in s:
    cnt, tmp=0, Counter(start)

    for c in w:
        if c in tmp: # 같으면
            tmp[c]-=1
            if not tmp[c]:
                del tmp[c]
        else: # 다르면
            cnt += 1

    if cnt < 2 and len(tmp)<2:
        ans += 1
print(ans)