"""
단축기 지정
문제: https://www.acmicpc.net/problem/1283
"""
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

dic = Counter()
record = []

for _ in range(n):
    # 입력
    string = input().rstrip().split()
    # 첫 글짜 단축기 지정 여부
    flag = True
    for i in range(len(string)):
        # 만약 문자가 이미 존재하면 건너뛰기
        if dic[string[i]]:
            continue

        # 없다면
        if not dic[string[i]]:
            dic[string[i]] += 1
            if string[i][0].upper() not in record:
                record.append(string[i][0].upper())
                string[i] = "[" + string[i][0] + "]" + string[i][1:]
                flag = False
                break

        # 단축기 지정이 끝났으면 그냥 break
        if not flag:
            break

    # 아직 첫 글짜 단축기 지정이 안됐으면 딕셔너리에 있던 다 탐색해야함
    if flag:
        for i in range(len(string)):
            for j in range(len(string[i])):
                if string[i][j].upper() not in record:
                    record.append(string[i][j].upper())
                    # j가 현재 탐색중이 문자의 마지막 글자가 아닌경우
                    if j != len(string[i]) - 1:
                        string[i] = string[i][:j] + "[" + string[i][j] + "]" + string[i][j+1:]
                    else:
                        string[i] = string[i][:j] + "[" + string[i][j] + "]"
                    flag = False
                    break
            if not flag:
                break
    print(" ".join(string))