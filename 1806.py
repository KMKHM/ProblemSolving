import sys

input = sys.stdin.readline

n, s = map(int, input().split())

# 수열
nums = list(map(int, input().split()))

# 투 포인터
left, right = 0, 1

temp = sum(nums[left:right+1])

# 수열의 길이
min_len = sys.maxsize

while left < right:
    if temp < s:
        right += 1
        temp += nums[right]
    elif temp >= s:
        min_len = min(min_len, len(nums[left:right+1]))
        left += 1
        temp -= nums[left]

print(min_len if min_len != sys.maxsize else 0)

