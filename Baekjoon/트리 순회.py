"""
https://www.acmicpc.net/problem/1991
"""
import sys

input = sys.stdin.readline

n = int(input())

graph = {}

for _ in range(n):
    p, c1, c2 = input().split()
    graph[p] = [c1, c2]

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(graph[node][0])
    preorder(graph[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(graph[node][0])
    print(node, end='')
    inorder(graph[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')