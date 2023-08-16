"""
그르다 김가놈
문제: https://www.acmicpc.net/problem/18113
"""
import sys

input = sys.stdin.readline

# 김밥수, 꼬다리 길이, 김밥조각의 최소개수
n, k, m = map(int, input().split())

# 김밥의 길이
cook = [int(input()) for _ in range(n)]

cook.sort(reverse=True)


def binary_search(limit):

    l, r = 1, limit

    ans = 0

    while l <= r:

        mid = (l+r) // 2

        if limit // mid < m:
            r -= 1

        elif limit // mid >= m:
            ans = mid
            l += 1

    return ans




# 자른 김밥의 전체 길이
cnt = 0

for num in cook:
    # 양쪽 꼬다리보다 작으면
    if num < 2 * k:
        if num - k <= k:
            continue
        else:
            cnt += (num - k)

    else:
        cnt += (num - 2*k)

if cnt == 0:
    print(-1)
    sys.exit(0)
else:
    print(binary_search(cnt))




