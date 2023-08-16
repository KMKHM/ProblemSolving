"""
Sliding Window Maximum
문제: https://leetcode.com/problems/sliding-window-maximum/description/
"""
from collections import deque
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# 정답
result = []

# 윈도우
window = deque()

# 현재 최대값
current_max = float('-inf')

for i, v in enumerate(nums):
    window.append(v)
    # k개원 원소를 먼저 넣는다.
    if i < k - 1:
        continue

    if current_max == float('-inf'):
        current_max = max(window)
    elif v > current_max:
        current_max = v

    result.append(current_max)

    if current_max == window.popleft():
        current_max = float('-inf')

print(window)
print(current_max)
print(result)

a = 10
b = a
a += 1
print(b, a)