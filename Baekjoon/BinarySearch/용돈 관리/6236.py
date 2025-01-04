import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = [int(input()) for _ in range(n)]

nums.sort()

left, right = 1, sum(nums)

def check(money):
    tmp = money
    cnt = 1
    for num in nums:
        if tmp < num:
            tmp = money
            cnt += 1
        tmp -= num
    print(money, cnt)
    return cnt

res = 0

while left <= right:
    mid = (left + right) // 2

    # if nums[-1] > mid:
    #     left = mid + 1
    #     continue

    count = check(mid)

    if count == m:
        res = mid
        right = mid - 1
    # elif count < m:
    #     right = mid - 1
    elif count > m or m < max(nums):
        left = mid + 1

print(res)