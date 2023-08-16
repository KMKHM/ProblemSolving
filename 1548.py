"""
부분 삼각 수열
문제: https://www.acmicpc.net/problem/1548
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

if n < 3:
    print(n)
    sys.exit(0)

# 정렬
nums.sort()

# 정답 => 예제 1번을 보면 삼각수열을 만족하지 않는데
answer = 0

# i는 가장 큰 수 전까지 탐색
for i in range(n-1):
    # j는 가장 큰 수부터 탐색 가장 작은 수까지 탐색
    for j in range(n-1, -1, -1):
        # 정렬된 수 앞의 2개를 더해 뒤의 수보다 작으면 뒤의 수는 탐색할 필요없다.
        if nums[i] + nums[i+1] <= nums[j]:
            continue
        # 더 크면 최대값을 갱신할 수 있다. => j가 뒤에 있을수록 큰 값인데 앞은 탐색할 필요없이 i~j의 숫자를 세어주면 된다.
        answer = max(answer, j-i+1)

print(answer)




