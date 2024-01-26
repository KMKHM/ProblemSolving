import sys

t = int(input())

"""
[[3, 4], [2, 3], [1, 2], [0, 1]] 힘 a[i][j] = i번째 요원의 힘
[[3, 4], [1, 3], [2, 3], [0, 1]] 민첩 b[i][j] = i번째 요원의 민첩
[[3, 6], [2, 5], [1, 2], [0, 1]] 지능 c[i][j] = i번째 요원의 지능
"""



def bt(level):
    global ans
    if level == n:
        if ability[0] == 0 or ability[1] == 0 or ability[2] == 0:
            return
        print(ans)
        return

    # 만약 힘이 n-2 보다 작게 채워졌다면
    if ability[0] < n - 2 and not visited_b[level] and not visited_c[level]:
        ability[0] += 1
        ans += a[level][1]
        visited_a[level] = 1
        bt(level + 1)
        visited_a[level] = 0
        ans -= a[level][1]
        ability[0] -= 1
    # 지능
    if ability[1] < n - 2 and not visited_a[level] and not visited_c[level]:
        ability[1] += 1
        ans += b[level][1]
        visited_b[level] = 1
        bt(level + 1)
        visited_b[level] = 0
        ans -= b[level][1]
        ability[1] -= 1
    # 민첩
    if ability[2] < n - 2 and not visited_a[level] and not visited_b[level]:
        ability[2] += 1
        ans += c[level][1]
        visited_c[level] = 1
        bt(level + 1)
        visited_c[level] = 0
        ans -= c[level][1]
        ability[2] -= 1
for _ in range(t):
    n = int(input())
    ans = 0
    a, b, c = [], [], []

    for i in range(n):
        ai, bi, ci = map(int, input().split())
        a.append([i, ai])
        b.append([i, bi])
        c.append([i, ci])

    a.sort(reverse=True, key=lambda x: x[1])
    b.sort(reverse=True, key=lambda x: x[1])
    c.sort(reverse=True, key=lambda x: x[1])
    nums = [a, b, c]

    visited_a = [0] * n
    visited_b = [0] * n
    visited_c = [0] * n
    ability = [0] * 3
    tmp = []
    if n < 3:
        print(-1)
    else:
        bt(0)
        print(ans)
        print("------")
