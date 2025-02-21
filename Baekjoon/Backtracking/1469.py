"""
숌 사이 수열
문제: https://www.acmicpc.net/problem/1469
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
nums.sort()

res = []

visited = [0] * n

# 조건2 판단 함수
def check(arr):
    for num in nums:
        idx1, idx2, cnt = 0, 0, 0
        for i in range(len(arr)):
            if arr[i] == num:
                if cnt == 0:
                    idx1 = i
                    cnt += 1
                else:
                    idx2 = i
                    break
        if idx2-idx1-1 != num:
            return False

    return True

def backtracking():

    if len(res) == 2*n:
        if check(res):
            print(*res)
            sys.exit(0)
        return

    for i in range(n):
        if visited[i] != 2:
            res.append(nums[i])
            visited[i]+=1
            backtracking()
            visited[i]-=1
            res.pop()

backtracking()
print(-1)