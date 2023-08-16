import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

cnt = 0

dic = defaultdict(list)

for _ in range(n):
    a = list(input().split())
    if a[0] == "1":
        for num in a[3:]:
            dic[a[1]].append(int(num))

    elif a[0] == "2":

        if a[1] not in dic:
            continue

        if len(dic[a[1]]) <= int(a[2]):
            cnt += sum(dic[a[1]])
            dic[a[1]] = list()

        else:
            dic[a[1]].sort(reverse=True)
            for i in range(int(a[2])):
                cnt += dic[a[1]][i]
            dic[a[1]] = dic[a[1]][int(a[2]):]


print(cnt)



