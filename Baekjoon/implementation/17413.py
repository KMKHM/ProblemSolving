"""
단어 뒤집기 2
문제: https://www.acmicpc.net/problem/17413
"""
s = input()

# <, > 를 위한 boolean 변수 초기화
flag = False

# 정답
answer = ""

temp = ""

# 입력받은 문자열 탐색
for char in s:
    # 거꾸로 뒤집어야 하는 상황
    if not flag:
        # 문자가 괄호라면
        if char == "<":
            # 정상으로 출력해야 하므로 flag변수 바꿔줌
            flag = True
            # temp 변수에 문자를 순서대로 더해줌
            temp += char
        # 공백이면
        elif char == " ":
            # temp 변수에 더해주고
            temp += char
            # answer에 반영
            answer += temp
            # 초기화
            temp = ""
        # 정상 문자면
        else:
            # flag가 False이므로 거꾸로 더해줌
            temp = char + temp

    # 정상으로 더해줘야 하는 상황
    else:
        temp += char
        # 닫는 괄호를 보면
        if char == ">":
            flag = False
            # 그 동안 temp변수에 정상적으로 더한 문자들을 더해줌
            answer += temp
            # temp 변수 초기화
            temp = ""


print(answer + temp)





