"""
스위치 끄고 켜기
문제: https://www.acmicpc.net/problem/1244
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

m = int(input())
# ---------------------

for _ in range(m):
    sex, num = map(int, input().split())

    # 남자일 때
    if sex == 1:
        for i in range(num-1, n, num):
            nums[i] = 0 if nums[i] == 1 else 1
    # 여자일 때
    else:
        if num == 0 or nums == n-1:
            continue

        num -= 1
        nums[num] = 0 if nums[num] == 1 else 1
        l, r = num -1, num + 1

        while (l >= 0 and r < n):
            # 대칭이면
            if nums[l] == nums[r]:
                # 값 바꿔줌
                nums[l] = nums[r] = 0 if nums[l] == 1 else 1
                l -= 1
                r += 1
            else:
                break

cnt = 0
for i in range(n):
    print(nums[i], end=" ")
    cnt += 1
    if cnt % 20 == 0:
        print()


