"""
찾기
문제: https://www.acmicpc.net/problem/1786
"""
import sys

input = sys.stdin.readline

t, p = input().rstrip(), input().rstrip()

def make_pi_table(s):
    pi_table = [0] * len(s)

    idx = 0

    for j in range(1, len(s)):
        while idx > 0 and s[j] != s[idx]:
            idx = pi_table[idx - 1]

        if s[j] == s[idx]:
            idx += 1
            pi_table[j] = idx
    return pi_table


def kmp(parent, pattern):
    pi_table = make_pi_table(pattern)

    n1, n2 = len(parent), len(pattern)

    idx = 0
    res = []
    cnt = 0
    for i in range(n1):

        while idx > 0 and parent[i] != pattern[idx]:
            idx = pi_table[idx - 1]

        if parent[i] == pattern[idx]:
            if idx == n2 - 1:
                res.append(i - n2 + 2)
                cnt += 1
                idx = pi_table[idx]
            else:
                idx += 1
    print(cnt)
    for p in res:
        print(p, end=" ")
kmp(t, p)