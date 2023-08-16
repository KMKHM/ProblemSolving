"""
설탕 배달
문제: https://www.acmicpc.net/problem/2839
"""
n = int(input())

cnt = 0

while n >= 0:
    if n % 5 == 0:
       cnt += n//5
       print(cnt)
       break
    n -= 3
    cnt += 1

print(cnt if n >=0 else -1)

