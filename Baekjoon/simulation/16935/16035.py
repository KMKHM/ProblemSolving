"""
배열 돌리기3
문제: https://www.acmicpc.net/problem/16935
"""

n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

op = list(map(int, input().split()))

# 1번
def reverse_up_down(array):
    return array[::-1]

# 2번
def reverse_left_right(array):
    new_arr = []
    for i in range(len(array)):
        new_arr.append(array[i][::-1])
    return new_arr

# 3번 오른쪽 회전
def rotate_right(arr):
    return [list(row)[::-1] for row in zip(*arr)]

# 4번 왼쪽 회전
def rotate_left(arr):
    return [list(row) for row in zip(*arr)][::-1]

# 5번 나누기
def divide_rotate_right(arr):
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            temp[i][j + m // 2] = arr[i][j]
    for i in range(n // 2):
        for j in range(m // 2, m):
            temp[i + n // 2][j] = arr[i][j]
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            temp[i][j - m // 2] = arr[i][j]
    for i in range(n // 2, n):
        for j in range(m // 2):
            temp[i - n // 2][j] = arr[i][j]
    return temp

# 5번 나누기
def divide_rotate_left(arr):
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            temp[i + n // 2][j] = arr[i][j]
    for i in range(n // 2, n):
        for j in range(m // 2):
            temp[i][j + m // 2] = arr[i][j]
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            temp[i - n // 2][j] = arr[i][j]
    for i in range(n // 2):
        for j in range(m // 2, m):
            temp[i][j - m // 2] = arr[i][j]
    return temp


for o in op:
    if o == 1:
        arr = reverse_up_down(arr)
    if o == 2:
        arr = reverse_left_right(arr)
    if o == 3:
        arr = rotate_right(arr)
        n, m = m, n
    if o == 4:
        arr = rotate_left(arr)
        n, m = m, n
    if o == 5:
        arr = divide_rotate_right(arr)
    if o == 6:
        arr = divide_rotate_left(arr)

