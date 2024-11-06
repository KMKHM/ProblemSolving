"""
즐거운 단어
문제: https://www.acmicpc.net/problem/2922
"""
s = input().rstrip()

# 즐거운 단어란, 모음(A,E,I,O,U)이 연속해서 3번, 자음(모음을 제외한 나머지 알파벳)이 연속해서 3번 나오지 않아야 한다. 또, L을 반드시 포함해야 한다
n = len(s)
m = s.count("_")
vowel = "AEIOU"
alpha = "BCDFGHJKLMNPQRSTVWXYZ"

idx = [i for i in range(n) if s[i] == "_"]

res=0

tmp=list(s)

def check_vowel(arr):
    cnt1, cnt2 =0, 0
    for c in arr:
        if c in vowel:
            cnt2=0
            cnt1+=1
            if cnt1 >= 3:
                return True
        elif c in alpha:
            cnt1=0
            cnt2+=1
            if cnt2 >= 3:
                return True
        else:
            cnt1=0
            cnt2=0
    return False

def bt(level):
    global res

    if len(tmp) >= 3:
        if check_vowel(tmp):
            return

    if level == m:
        if not check_vowel(tmp) and "L" in tmp:
            res+=1
        return

    for c in alpha + vowel:
        tmp[idx[level]] = c
        bt(level+1)
        tmp[idx[level]] = "_"

bt(0)
print(res)