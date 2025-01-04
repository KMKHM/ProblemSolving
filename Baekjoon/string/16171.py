"""
나는 친구가 적다 (Small)
문제: https://www.acmicpc.net/problem/16171
"""
import sys

s=input().rstrip()
target=input().rstrip()

string = "".join(i for i in s if i.isalpha())

for i in range(len(string)):
    if string[i:]==target:
        print(1)
        sys.exit(0)
print(0)