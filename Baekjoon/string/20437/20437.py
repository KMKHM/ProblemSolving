"""
문자열 게임 2
문제: https://www.acmicpc.net/problem/20437
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w = input().rstrip()
    k = int(input())

    # 각 문자의 위치를 저장
    char_positions = defaultdict(list)
    for i, char in enumerate(w):
        char_positions[char].append(i)

    min_length = float('inf')
    max_length = -1

    for char, positions in char_positions.items():
        # 해당 문자가 K개 이상 있는 경우만 확인
        if len(positions) >= k:
            # K개씩 슬라이딩 윈도우로 확인
            for i in range(len(positions) - k + 1):
                current_length = positions[i + k - 1] - positions[i] + 1

                min_length = min(min_length, current_length)

                if w[positions[i]] == w[positions[i + k - 1]]:
                    max_length = max(max_length, current_length)

    if min_length == float('inf') or max_length == -1:
        print(-1)
    else:
        print(min_length, max_length)
