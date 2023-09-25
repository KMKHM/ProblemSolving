s = input()

# 맞춰야하는 문자
possible = "quack"

s = list(s)

# 문자 길이
n = len(s)

# 정답
ans = 0

# 모든 문자 탐색해야 함
while n > 0:
    # 문자 완성여부 체크
    check = False
    # 완성해야 할 문자열 인덱스와 현재 탐색하고 있는 문자열 인덱스
    target, cur = 0, 0
    temp = [0] * 5
    # 0부터 원래 길이 까지만 탐색해야 함 => 한 번 탐색끝낼 때 마다 오리 한 마리씩 추가함
    while cur < len(s):
        if s[cur] == possible[target]:
            temp[target] = cur
            target += 1
            # 목표하는 문자의 길이가 되면 변수 초기화
            if target == 5:
                check = True
                # 5개 탐색했으니 원래 길이에서 5개 빼줌
                n -= 5
                target = 0
                # 원래 배열에 있던 quack 지워줌
                for i in range(5):
                    s[temp[i]] = "_"
        # 다르면 그냥 현재 인덱스 추가해주면서 탐색
        else:
            cur += 1

    if check:
        ans += 1
    # 완성하지 못한 게 하나라도 있으면 바로 break
    else:
        break

# n 남으면 어차피 남은 문자가 있으므로 -1 넣어주면 됨
ans = ans if not n else -1

# 정답 출력
print(ans)