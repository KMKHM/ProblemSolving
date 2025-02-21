"""
오리
문제: https://www.acmicpc.net/problem/12933
"""
import sys

s = input()
# k가 나오기전에 q가 나오면 + 1
# k가 끝나고 q가 나오면 그냥 넘어감

# 딕셔너리에 순서 유지되는지 확인
dic = {"q": 0, "u": 0, "a": 0, "c": 0, "k": 0}
def check():
    if dic["u"] and not dic["q"]:
        return False
    if dic["a"] and (not dic["q"] or not dic["u"]):
        return False
    if dic["c"] and (not dic["q"] or not dic["u"] or not dic["a"]):
        return False
    if dic["k"] and (not dic["q"] or not dic["u"] or not dic["a"] or not dic["c"]):
        return False
    return True

ans = 0

for i in range(len(s)):
    if s[i] == "q": # q일 때
        # k가 없으면 그냥 1마리 추가해줌
        if not dic["k"]:
            dic[s[i]] += 1
            ans += 1
        else:
            dic[s[i]] += 1
            for char in "quack":
                dic[char] -= 1

    if s[i] == "k":
        dic[s[i]] += 1
        if not check():
            print(-1)
            sys.exit(0)

    if s[i] == "c":
        dic[s[i]] += 1
        if not check():
            print(-1)
            sys.exit(0)

    if s[i] == "a":
        dic[s[i]] += 1
        if not check():
            print(-1)
            sys.exit(0)

    if s[i] == "u":
        dic[s[i]] += 1
        if not check():
            print(-1)
            sys.exit(0)

if dic["q"] == dic["u"] == dic["a"] == dic["c"] == dic["k"]:
    print(ans)
else:
    print(-1)





