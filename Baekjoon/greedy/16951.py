import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))

answer = 0

for i in range(n-1):
    if nums[i+1] - nums[i] != k:
        if nums[i+1] <= nums[i]:
            nums[i+1] = nums[i] + k
            answer += 1
        else:
            if nums[i+1] - k > 1:
                nums[i+1] -= k
                answer += 1
            else:
                nums[i] = nums[i+1] - k

print(answer)
