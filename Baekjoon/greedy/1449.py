"""
수리공 항승
문제: https://www.acmicpc.net/problem/1449
"""
import sys

input = sys.stdin.readline

n, l = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

start = nums[0]

ans = 1

for i in nums[1:]:
    # 만약 시작구간부터 L 떨어진 거리만큼 물이 새는 곳이 범위에 있다면 테이프 개수 늘려줄 필요가 없다.
    if i in range(start, start + l):
        continue

    # 1~2구간에서 100~101구간으로 이동하기 위해 시작지점을 아애 바꿔주고 테이프 개수를 늘려준다.
    else:
        start = i
        ans += 1

print(ans)
s = "A___quick__brown__fox__jumps__over__the__lazy__dog"
print(len(s))