"""
넴모넴모 (Easy)
문제: https://www.acmicpc.net/problem/14712
"""
n,m=map(int,input().split())
nemo=[[0]*(m+1) for _ in range(n+1)]
answer=0

def dfs(depth):
    global answer
    if(depth==n*m):
        answer+=1
        return
    x=depth//m+1
    y=depth%m+1

    if(nemo[x-1][y]==0 or nemo[x-1][y-1]==0 or nemo[x][y-1]==0):
        # 넴모를 놓을 수 있는 경우
        nemo[x][y]=1
        dfs(depth+1)
        nemo[x][y]=0 #되돌아오면 다시 0
    dfs(depth+1) # 넴모를 안 놓음

dfs(0)
print(answer)
