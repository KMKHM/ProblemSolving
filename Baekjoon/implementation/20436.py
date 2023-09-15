"""
ZOAC 3
문제: https://www.acmicpc.net/problem/20436
"""
sl, sr = input().split()

s = input().rstrip()

tmp = ""

key = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]


left, right = ["q", "w", "e", "r","t" ,"a", "s", "d", "f", "g", "z", "x", "c", "v"], ["y","u","i","o","p","h","j","k","l","b","n","m"]

sl_index = [0, 0]
for i in range(len(key)):
    if sl in key[i]:
        sl_index[0] = i
        sl_index[1] = key[i].index(sl)

sr_index = [0, 0]
for i in range(len(key)):
    if sr in key[i]:
        sr_index[0] = i
        sr_index[1] = key[i].index(sr)

ans = 0

for i in range(len(s)):
    if s[i] in left:
        for r in range(len(key)):
            if s[i] in key[r]:
                ans += abs(sl_index[0]-r) + abs(sl_index[1]-key[r].index(s[i])) + 1
                sl_index[0] = r
                sl_index[1] = key[r].index(s[i])

    else:
        for r in range(len(key)):
            if s[i] in key[r]:
                ans += abs(sr_index[0]-r) + abs(sr_index[1]-key[r].index(s[i])) + 1
                sr_index[0] = r
                sr_index[1] = key[r].index(s[i])



print(ans)


