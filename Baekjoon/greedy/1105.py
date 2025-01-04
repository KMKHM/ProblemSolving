"""
팔
문제: https://www.acmicpc.net/problem/1105
"""

L, R = input().split()

cnt=0

if len(L)==len(R):

    for i in range(len(L)):
        if L[i] != R[i]:
            break
        else:
            if L[i] == '8':
                cnt+=1

print(cnt)