from collections import deque

s = input().rstrip()
t = input().rstrip()

"""
s <-> t
"""

q = deque(list(t))

while 1:
    if q[0] == q[-1] == "A":
        q.pop()
    elif q[0] == q[-1] == "B":
        q.popleft()
        q.reverse()
    else:
        break
    print(q)
print(q)

