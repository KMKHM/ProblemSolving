"""
개구리 1
문제: https://www.acmicpc.net/problem/15566
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 음식, 취미, 가족, 철학에 대한 흥미도
frog_interesting = []

for i in range(n):
    frog_interesting.append(list(map(int, input().split())))

# 개구리 배치도
order = [0] * n

visited = [0] * n

# 선호하는 연꽃 번호
frog_flower = []

for i in range(n):
    a, b = map(int, input().split())
    frog_flower.append([a-1, b-1])

    # 먼저 개구리가 선호하는 연꽃의 번호가 하나인 자리 채우기
    if a == b:
        frog_flower[i][1] = -1

# 통나무
log = []

for _ in range(m):
    a, b, t = map(int, input().split())
    log.append([a-1, b-1, t-1])

# 흥미도 검사
def check():
    for i in range(m):
        # 선호하는 연꽃 두개와 대화 주제
        a, b, t = log[i][0], log[i][1], log[i][2]
        # 개구리 두마리
        frog1, frog2 = order[a], order[b]
        # 대화 주제의 흥미도가 틀리면 바로 False 리턴
        if frog_interesting[frog1][t] != frog_interesting[frog2][t]:
            return False

    return True

def backtracking(level):
    # 만약 8개 다 채웠으면 리턴
    if level == n:
        if check():
            print("YES")
            for num in order:
                print(num+1, end = " ")
            sys.exit(0)
        return

    for i in range(2):
        if frog_flower[level][i] == -1:
            continue


        tmp = frog_flower[level][i]

        if not visited[tmp]:
            visited[tmp] = 1
            order[tmp] = level
            backtracking(level + 1)
            visited[tmp] = 0


backtracking(0)

print("NO")