"""
나무꾼 이다솜
문제: https://www.acmicpc.net/problem/1421
"""
import sys

input = sys.stdin.readline

n, c, w = map(int, input().split())

wood = [int(input()) for _ in range(n)]

left, right = 1, max(wood)

ans = 0

while left <= right:
    mid = (left + right) // 2

    tmp_sum = 0
    tmp_cnt = 0
    tmp_cost = 0

    for i in wood:
        q, r = divmod(i, mid)
        if r:
            tmp_cost += q * c
        else:
            tmp_cost += (q - 1) * c
        target = q * w * mid - tmp_cost
        if target < 0:
            continue
        else:
            tmp_sum += target

    if tmp_sum >= ans:
        ans = tmp_sum
        print(mid, ans)
        left = mid + 1
    elif tmp_sum < ans:
        right = mid - 1

print(ans)

tmp = 6
ts = 0
cnt = 0
cost = 0
for a in wood:
    cnt += (a//tmp)
    print(cnt)
    cost += (a//tmp)
ts = cnt * tmp * w - cost * c
print(ts)