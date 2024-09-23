"""
List of Unique Numbers
문제: https://www.acmicpc.net/problem/13144
"""
n = int(input())
arr = list(map(int, input().split()))

s = e = cnt = 0
num_dict = {}

while e < n:
    print(num_dict)
    print(s, e)
    print(cnt)
    if arr[e] not in num_dict:
        num_dict[arr[e]] = 1
        e += 1
        cnt += e - s
    else:
        del num_dict[arr[s]]
        s += 1

print(cnt)

