"""
ZOAC
문제: https://www.acmicpc.net/problem/16719
"""
s = list(input().rstrip())

# 정답
res = [""] * len(s)

def bt(arr, start):
    if not arr:
        return

    min_s = min(arr)
    idx = arr.index(min_s)

    res[start + idx] = min_s
    print("".join(res))

    bt(arr[idx+1:], start + idx + 1)
    bt(arr[:idx], start)

bt(s, 0)

