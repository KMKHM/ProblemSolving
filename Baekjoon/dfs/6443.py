import sys

input = sys.stdin.readline

word = []

n = int(input())

for _ in range(n):
    word.append(input().rstrip())

res = {}

def dfs(string, visited):
    length = len(string)

    if len(comb) == length:
        if "".join(comb) not in res:
            res["".join(comb)] = 1
        return

    for i in range(length):
        if not visited[i]:
            comb.append(string[i])
            visited[i] = 1
            dfs(string, visited)
            visited[i] = 0
            comb.pop()


for string in word:
    comb = []
    dfs(sorted(string), [0] * len(string))


answer = res.keys()
for s in answer:
    print(s)


