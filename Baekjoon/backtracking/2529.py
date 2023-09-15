"""
부등호
문제: https://www.acmicpc.net/problem/2529
"""
import sys
input = sys.stdin.readline

n = int(input())

s = input().split()

res = []

def check(arr):
    for k in range(len(arr)-1):
        if s[k] == "<":
            if not (arr[k] < arr[k+1]):
                return False
        else:
            if not (arr[k] > arr[k+1]):
                return False
    return True
ans = []
def bt(idx):
    if idx == n+1:
        ans.append(res[:])
        return

    if len(res) > 1:
        if not check(res):
            return

    for i in range(10):
        if i not in res:
            res.append(i)
            bt(idx+1)
            res.pop()


bt(0)
def a(l):
    tmp = ""
    for i in l:
        tmp += str(i)
    return tmp
print(a(ans[-1]))
print(a(ans[0]))
