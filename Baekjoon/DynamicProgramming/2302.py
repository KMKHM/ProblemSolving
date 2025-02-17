n = int(input())

dp = [1] * (n+1)


check = [0] * (n+1)

m = int(input())

for _ in range(m):
    check[int(input())] = 1

for i in range(1, n+1):
    if check[i]:
        dp[i] = dp[i-1]
        continue

    if i == 1:
        if not check[i+1]:
            dp[i] = 2
        else:
            dp[i] = 1

    elif i == n:
        if not check[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    else:
        if not check[i-1] and not check[i+1]:
            dp[i] = dp[i-1] * 2

        elif not check[i-1] or not check[i+1]:
            dp[i] = i

        else:
            dp[i] = dp[i-1]


print(dp)