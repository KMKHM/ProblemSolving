"""
부분 수열의 합
문제: https://www.acmicpc.net/problem/1182
"""
n, s = map(int, input().split())


visited = [0] * n
nums = list(map(int, input().split()))

res = []

ans = 0
def bt(level):
    global ans

    if level > 0:
        if sum(res) == s:
            ans += 1


    for i in range(level, n):
        if not visited[i]:
            visited[i] = 1
            res.append(nums[i])
            bt(i+1)
            visited[i] = 0
            res.pop()
bt(0)

print(ans)