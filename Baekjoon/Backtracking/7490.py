"""
0 만들기
문제: https://www.acmicpc.net/problem/7490
"""
import copy, sys

sys.setrecursionlimit(10**9)

t = int(input())


def backtracking(l, arr1):
    if l == n:
        arr = copy.deepcopy(arr1)
        temp = arr[0]
        if " " in arr:
            while " " in arr:
                idx = arr.index(" ")
                arr[idx] = arr[idx-1] + arr[idx+1]
                arr.remove(arr[idx-1])
                arr.remove(arr[idx])


        s = "".join(arr)
        temp = eval(s)

        if temp == 0:
            a.append("".join(arr1))
            return
        return


    backtracking(l+1, arr1 + ["+"] + [str(l+1)])
    backtracking(l+1, arr1 + ["-"] + [str(l+1)])
    backtracking(l+1, arr1 + [" "] + [str(l+1)])


for _ in range(t):
    a = []
    n = int(input())
    backtracking(1, [str(1)])
    a.sort()
    for i in a:
        print(i)
    print()