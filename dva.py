def knapsack_multiple_people(values, weights, W, num_people):
    n = len(values)
    # DP 테이블 초기화
    dp = [[[0 for _ in range(W + 1)] for _ in range(num_people + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for p in range(1, num_people + 1):
            for w in range(W + 1):
                # 물건 i를 선택하지 않는 경우
                dp[i][p][w] = dp[i - 1][p][w]
                # 물건 i를 선택하는 경우
                if w >= weights[i - 1]:
                    dp[i][p][w] = max(dp[i][p][w], dp[i - 1][p - 1][w - weights[i - 1]] + values[i - 1])

    # 각 사람의 최적 해를 구함
    max_values = [dp[n][p][W] for p in range(1, num_people + 1)]

    return max_values


# 예시 입력
values = [5, 4, 1, 7, 1]
weights = [4, 3, 2, 5, 1]
W = 7
num_people = 2
print(knapsack_multiple_people(values, weights, W, num_people))  # [7, 6] 출력 예상
