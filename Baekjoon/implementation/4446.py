"""
ROT13
문제: https://www.acmicpc.net/problem/4446
"""

vowel="aiyeou"
not_vowel="bkxznhdcwgpvjqtsrlmf"


while 1:
    try:
        s = input().rstrip()
        res = ""
        for c in s:
            if not c.isalpha():
                res+=c
                continue
            flag=True
            if c.isupper():
                flag=False
                c=c.lower()

            if c in vowel:
                c=vowel[vowel.index(c)-3]
            else:
                c=not_vowel[not_vowel.index(c)-10]

            res += c if flag else c.upper()
        print(res)
    except:
        break