"""
이모티콘
문제: https://www.acmicpc.net/problem/14226
"""
import sys
from collections import deque
s = int(input())

# 복사 => 1초
# 붙여넣기 => 1초
# 화면의 이모티콘 중 하나 삭제

visited = dict()

# 복사 + 붙여넣기 => 2초

def bfs(cur):
    q = deque()
    # 현재 개수, 클립보드에 있는 것
    q.append([cur, 0])
    visited[(cur, 0)] = 0

    while q:
        # 현재 개수, 클립보드에 있는 개수,
        now, clipboard = q.popleft()
        if now == s:
            print(visited[(now, clipboard)])
            sys.exit(0)

        # 복사
        if (now, now) not in visited:
            visited[(now, now)] = visited[(now, clipboard)] + 1
            q.append((now, now))
        if (now + clipboard, clipboard) not in visited:
            visited[(now + clipboard, clipboard)] = visited[(now, clipboard)] + 1
            q.append((now + clipboard, clipboard))
        if (now - 1, clipboard) not in visited:
            visited[(now - 1, clipboard)] = visited[(now, clipboard)] + 1
            q.append((now - 1, clipboard))

bfs(1)
