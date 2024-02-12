"""
보석 상자
문제: https://www.acmicpc.net/problem/2792
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [int(input()) for _ in range(m)]

start = 1
end = sum(nums)

ans = 1e9

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    tmp = 0

    for num in nums:
        count = num // mid
        cnt += count
        # 학생이 가져가는 개수
        tmp = max(tmp, count)

    if tmp > ans:
        end = mid - 1
    elif tmp <= ans:
        ans = tmp
        start = mid + 1

print(ans)


