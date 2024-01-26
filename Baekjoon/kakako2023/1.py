# 이번달에 선물을 더 많이 준 사람이 다음 달에 선물을 하나 받는다
# 같거나 없으면 선물지수가 큰 사람이 작은 사람에게 선물을 받는다, / 선물지수같으면 다음 달 선물 주고 받지 않는다.
# 준 선물 = 3, 받은 선물 = 10 => 지수 = -7

from collections import defaultdict

friends = ["muzi", "ryan", "frodo", "neo"]

gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi",
         "frodo muzi", "frodo ryan", "neo muzi"]


# 준 선물 수
give_dic = dict()

# 받은 선물 수
take_dic = dict()

# 선물 준 기록
pre = defaultdict(list)

for r in gifts:
    a, b = r.split()
    # 선물 준 횟수, 받은 횟수 기록
    if a not in give_dic:
        give_dic[a] = 1
    else:
        give_dic[a] += 1

    if b not in take_dic:
        take_dic[b] = 1
    else:
        take_dic[b] += 1
    # 선물 준 기록
    pre[a].append(b)

print(give_dic)
print(take_dic)
print(pre)


# 정답 딕셔너리
ans_dic = dict()

for f in friends:
    ans_dic[f] = 0

record = defaultdict(list)

for a in friends:
    for b in friends:
        # 같은 사람이면 무시
        if a == b:
            continue

        # b 가 a 레코드에 있거나 a가 b레코드에있으면
        if b in record[a] or a in record[b]:
            continue
        # 선물받은기록
        record[a].append(b)

        # print(pre[a].count(b), pre[b].count(a))
        # a가 b에게 준 선물보다 b가 a에게 준 선물이 더 많으면 b가 선물 받아야 함
        if pre[a].count(b) < pre[b].count(a):
            ans_dic[b] += 1
        elif pre[b].count(a) < pre[a].count(b):
            ans_dic[a] += 1
        elif (pre[a].count(b) == 0 and pre[b].count(a) == 0) or pre[a].count(b) == pre[b].count(a): # 선물 기록이 없는 경우
            # 선물 지수
            cnt_a = (give_dic[a] if a in give_dic else 0) - (take_dic[a] if a in take_dic else 0)
            cnt_b = (give_dic[b] if b in give_dic else 0) - (take_dic[b] if b in take_dic else 0)
            if cnt_a < cnt_b:
                ans_dic[b] += 1
            elif cnt_a > cnt_b:
                ans_dic[a] += 1
        # elif pre[a].count(b) == pre[b].count(a): # 선물 기록이 같거나 없는 경우
        #     # 선물 지수
        #     cnt_a = (give_dic[a] if a in give_dic else 0) - (take_dic[a] if a in take_dic else 0)
        #     cnt_b = (give_dic[b] if b in give_dic else 0) - (take_dic[b] if b in take_dic else 0)
        #     if cnt_a < cnt_b:
        #         ans_dic[b] += 1
        #     elif cnt_a > cnt_b:
        #         ans_dic[a] += 1


print(ans_dic)

