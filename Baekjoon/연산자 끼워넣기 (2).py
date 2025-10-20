"""
https://www.acmicpc.net/problem/15658
"""
import sys

input = sys.stdin.readline

n=int(input())

arr = list(map(int, input().split()))

op = list(map(int, input().split()))
val1, val2 = -sys.maxsize, sys.maxsize

def bt(num, idx):
    global val1, val2

    if idx == n-1:
        val1 = max(num, val1)
        val2 = min(num, val2)
        return

    if op[0]:
        op[0]-=1
        bt(num+arr[idx+1], idx+1)
        op[0]+=1

    if op[1]:
        op[1]-=1
        bt(num-arr[idx+1], idx+1)
        op[1]+=1

    if op[2]:
        op[2]-=1
        bt(num*arr[idx+1], idx+1)
        op[2]+=1

    if op[3]:
        op[3]-=1
        bt(int(num/arr[idx+1]), idx+1)
        op[3]+=1

bt(arr[0], 0)
print(val1)
print(val2)