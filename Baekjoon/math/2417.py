"""
정수 제곱근
문제: https://www.acmicpc.net/problem/2417
"""
n = int(input())

if int(n**(0.5)) ** 2 >= n:
    print(int(n**(0.5)))
else:
    print(int(n**(0.5))+1)