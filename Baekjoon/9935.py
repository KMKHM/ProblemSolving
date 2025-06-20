import sys

input = sys.stdin.readline

total, sub = input().rstrip(), input().rstrip()

n, m = len(total), len(sub)

s = []
for ch in total:
    s.append(ch)
    if len(s) >= m and ''.join(s[-m:]) == sub:
        for _ in range(m):
            s.pop()

print(''.join(s) if s else "FRULA")