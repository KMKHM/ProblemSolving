from itertools import combinations
n = int(input())
tmp = list(map(int,input().split()))
calculation = list(map(int,input().split()))
calculationLst = []
res = []

# 연속된 수식어 리스트 구하기
for idx,val in enumerate(calculation):
    if idx == 0:
        if val > 0:
            for i in range(val):
                calculationLst.append('+')
    elif idx == 1:
        if val > 0:
            for i in range(val):
                calculationLst.append('-')
    elif idx == 2:
        if val > 0:
            for i in range(val):
                calculationLst.append('*')
    else:
        if val > 0:
            for i in range(val):
                calculationLst.append('/')

visited = [False] * (len(calculationLst) + 1)

def dfs(start, tlst):

    if len(tlst) == len(calculationLst):
        print(tlst)
        ans = tmp[0]
        for i in range(1,len(calculationLst)+1):
            express = ord(tlst[i-1])
            if express == 43: # +
                ans = (tmp[i] + ans)
            elif express == 45: # -
                ans = (ans - tmp[i])
            elif express == 42: # *
                ans = (tmp[i] * ans)
            elif tmp[i] == 0 or ans == 0:
                pass
            elif express == 47: # /
                ans = int(ans / tmp[i])

        res.append(ans)
        return

    for i in range(1,len(calculationLst)+1):
        if visited[i] == False:
            visited[i] = True
            dfs(start+1,tlst + [calculationLst[i-1]])
            visited[i] = False



dfs(0,[])
print(max(res))
print(min(res))