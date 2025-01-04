"""
문서 검색
문제: https://www.acmicpc.net/problem/1543
"""
document = input().rstrip()
target = input().rstrip()

print(document.count(target))