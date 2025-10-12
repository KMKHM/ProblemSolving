"""
https://www.acmicpc.net/problem/9421
"""
n = int(input())

res = [0] * (n+1)

def transform(num):
    val = 0
    while num:
        val += (num % 10) ** 2
        num //= 10
    return val

# 에라토스테네스의 체
arr = [1] * (n+1)
arr[0] = arr[1] = 0

for i in range(2, int(n**0.5) + 1):
    for j in range(i+i, n+1, i):
        if arr[i]:
            arr[j] = 0


for i in range(1, n+1):
    if res[i]:
        continue
    if arr[i]:
        num = i
        temp = set()
        temp.add(i)
        flag = True
        while True:
            num = transform(num)
            if num in temp:
                flag = False
                break
            elif num == 1:
                break
            temp.add(num)
        if flag:
            # print(i, temp)
            for e in temp:
                if e <= n and arr[e]:
                    res[e] = 1

for i in range(1, n+1):
    if res[i]:
        print(i)