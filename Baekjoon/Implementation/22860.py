import sys
from collections import defaultdict

input = sys.stdin.readline

# 폴더의 총 개수, 파일의 총 개수
n, m = map(int, input().split())

main = set()

for _ in range(n+m):
    a, b, c = input().split()
    if a == "main" and c == "1":
        main.add(b)
    elif a == "main" and c == "0":
        main.add
