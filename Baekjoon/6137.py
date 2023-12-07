"""
문자열 생성
문제: https://www.acmicpc.net/problem/6137
"""
import sys

input = sys.stdin.readline

n = int(input())

s = [input().rstrip() for _ in range(n)]

t = ""

left, right = 0, n - 1

while left <= right:
    if s[left] < s[right]:
        t += s[left]
        left += 1
    elif s[right] < s[left]:
        t += s[right]
        right -= 1
    # 같은 경우
    else:
        tmp_l, tmp_r = left + 1, right - 1
        flag = True
        while tmp_l <= tmp_r:
            if s[tmp_l] < s[tmp_r]:
                flag = True
                break
            if s[tmp_r] < s[tmp_l]:
                flag = False
                break
            tmp_l += 1
            tmp_r -= 1

        if flag:
            t += s[left]
            left += 1
        else:
            t += s[right]
            right -= 1

cnt = 0
for char in t:
    print(char, end="")
    cnt += 1
    if cnt % 80 == 0:
        print()