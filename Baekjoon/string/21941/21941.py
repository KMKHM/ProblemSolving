"""
문자열 제거
문제: https://www.acmicpc.net/problem/21941
"""
import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())

dic = {}
for _ in range(n):
    word, score = input().split()
    dic[word] = int(score)

dp = [0] * (len(s) + 1)

for i in range(1, len(s) + 1):
    dp[i] = dp[i - 1] + 1  # 그냥 한 글자 제거 (1점)
    for word in dic:
        l = len(word)
        if i >= l and s[i - l:i] == word:
            dp[i] = max(dp[i], dp[i - l] + dic[word])

print(dp[len(s)])
