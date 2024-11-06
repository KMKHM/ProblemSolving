"""
카드 놓기
문제: https://www.acmicpc.net/problem/5568
"""
import sys

input = sys.stdin.readline

n = int(input())

k = int(input())

nums = [int(input()) for _ in range(n)]

check = [0] * n

res = set()

def bt(cur, cnt):
    # k개의 카드를 선택한 경우
    if cnt == k:
        res.add(cur)  # 선택한 카드 조합을 결과에 추가
        return

    for i in range(n):
        if not check[i]:  # 아직 사용하지 않은 카드일 때
            check[i] = 1  # 카드를 선택 상태로 변경
            bt(cur + str(nums[i]), cnt + 1)  # 현재 카드 추가 및 개수 증가
            check[i] = 0  # 백트래킹: 선택을 해제하고 다음 카드로 이동

bt("", 0)

print(len(res))