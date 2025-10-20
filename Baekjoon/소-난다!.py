"""
https://www.acmicpc.net/problem/19699
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

num = sum(arr)

prime=[1]*(num+1)

prime[0]=prime[1]=0

for i in range(2, int(num**0.5)+1):
    if prime[i]:
        for j in range(i*2, num+1, i):
            prime[j] = 0

res=set()
check=[0]*n
def bt(idx, ls):
    if len(ls) == m:
        val = sum(ls)
        if prime[val]:
            res.add(val)
        return

    for i in range(idx, n):
        if not check[i]:
            check[i]=1
            ls.append(arr[i])
            bt(i+1, ls)
            ls.pop()
            check[i]=0

bt(0,[])

if res:
    print(*sorted(res))
else:
    print(-1)