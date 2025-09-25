"""
원숭이 매달기
문제: https://www.acmicpc.net/problem/2716
"""
import sys

tc = int(sys.stdin.readline().strip())

for _ in range(tc):
    op = sys.stdin.readline()

    maxDepth = 0
    tree = list()
    for o in op:
        if o == ']':
            maxDepth = max(len(tree), maxDepth)
            tree.pop()
        else:
            tree.append('[')

    print(2**maxDepth)