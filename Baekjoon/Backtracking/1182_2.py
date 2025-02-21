n,s = map(int,input().split())
arr = list(map(int,input().split()))

# 6 6
# 1 2 3 4 5 6
def dfs(level, count):
    global answer

    # 모든 경우의 수를 탐색했을 때의 상태 트리
    if level == n:
        if count == s:
            answer += 1
        return

    dfs(level + 1, count + arr[level])
    dfs(level + 1, count)

level = 3, [1, 2, 3]
level = 4, [1, 2, 3]
level = 5, [1, 2, 3]
level = 6, [1, 2, 3]




answer = 0


dfs(0, 0)

if s == 0:
    answer -= 1
print(answer)