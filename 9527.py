"""
1의 개 세기
문제: https://www.acmicpc.net/problem/9527
"""
a, b = map(int, input().split())

ans = 0

# a = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

for i in range(a, b+1):
    print(i, bin(i))
    ans += bin(i).count('1')

# 2**0 2**1
x,y=0,1

while not (2**x<= a <= 2**y):
    x+=1
    y+=1

# while a != b:


print(x, y)