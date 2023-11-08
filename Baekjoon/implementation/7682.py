"""
틱택토
문제: https://www.acmicpc.net/problem/7682
"""
import sys

input = sys.stdin.readline


# .이 없을 때
def check1(arr):
    # 1) o의 개수가 x보다 많으면 무조건 잘못됨
    if arr.count("X") < arr.count("O"):
        return False
    # 2) o의 개수가 x의 개수와 차이가 1이 아니면 잘못됨
    if arr.count("X") - 1 != arr.count("O"):
        return False


# 가로 세로 대각선 판단
def check2(arr):
    # 가로
    for i in range(0, 9, 3):
        # 전부 X 인 경우
        if "O" not in arr[i:i+3] and "." not in arr[i:i+3]:
            return True
        # 전부 O 인 경우
        if "X" not in arr[i:i+3] and "." not in arr[i:i+3]:
            return True
    # 세로 036 147 258
    for i in range(3):
        # 전부 X 인 경우
        if "O" not in [arr[i], arr[i+3], arr[i+6]] and "." not in [arr[i], arr[i+3], arr[i+6]]:
            return True
        # 전부 O 인 경우
        if "X" not in [arr[i], arr[i+3], arr[i+6]] and "." not in [arr[i], arr[i+3], arr[i+6]]:
            return True

    # 대각선
    # 전부 X 인 경우
    if "O" not in [arr[0], arr[4], arr[8]] and "." not in [arr[2], arr[4], arr[6]]:
        return True
    # 전부 O 인 경우
    if "X" not in [arr[0], arr[4], arr[8]] and "." not in [arr[2], arr[4], arr[6]]:
        return True

while True:
    s = input().rstrip()

    if s == "end":
        sys.exit(0)

    # o의 개수가 많은 경우는 없다.
    if s.count("X") < s.count("O"):
        print("invalid")
        continue
    # .이 없을 때
    if "." not in s:
        # 만약 o, x의 차이가 1이 아니면 무조건 틀림
        if s.count("X") - 1 != s.count("O"):
            print("invalid")
            continue
        


