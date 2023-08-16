import sys
from collections import deque

input = sys.stdin.readline



# 크레인 수
n = int(input())

# 크레인 제한
nums = sorted(list(map(int, input().split())), reverse=True)


m = int(input())

box = deque(sorted(list(map(int, input().split())), reverse=True))

if nums[0] < box[0]:
    print(-1)
    sys.exit(0)

# 정답
ans = 0

check = [0] * m

while box:
    ans += 1
    for num in nums:
        for b in box:
            if num >= b:
                box.popleft()
                break


print(ans)







