"""
금민수의 개수
문제: https://www.acmicpc.net/problem/1527
"""
from collections import defaultdict
a, b = map(int, input().split())

dic = defaultdict(list)

n = len(str(b))

dic[1] = ["4", "7"]
for i in range(2, n + 1):
    dic[i] = ["4" + a for a in dic[i-1]] + ["7" + a for a in dic[i-1]]


cnt = 0

for i, j in dic.items():
    for num in j:
        if a <= int(num) <= b:
            cnt += 1

print(cnt)