from collections import deque

coins = 4

cards = [3, 6, 7, 2, 1, 10, 6, 9, 8, 12, 11, 4]

n = len(cards)

limit = n + 1

# 초기
init = cards[:n//3]

# 나머지 카드
remain = deque(cards[n//3:])

def check(arr, a, b):
    arr.append(a)
    arr.append(b)
    for num in arr:
        if limit-num in arr:
            return True
    return False

while coins and remain:
    if check(coins, remain[0], remain[1]):
        continue





# def recursive():
#     global ans, a, b
#
#     if coins == 0:
#         return
#
#     for _ in range(2):
#         if coins:
#             init.append(remain.popleft())
#
#     for num in sorted(coins):
#         if limit - num in coins:
#             a, b = num, limit - num
#             break
#
#     init.remove(a)
#     init.remove(b)
#     a, b = 0, 0




