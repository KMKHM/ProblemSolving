from itertools import combinations, product
from collections import Counter

a = [1, 2, 3, 4]

dice = [[1,2,3,4,5,6], [3,3,3,3,4,4], [1,3,3,4,4,4], [1,1,4,4,5,5]]
nums = list(enumerate(dice))
# print(nums)

ans, ans_list = 0, []

for a in list(combinations(nums, len(nums)//2)):
    win = 0
    # 전체 인덱스
    total = set([i for i in range(len(dice))])
    # 뽑은 인덱스
    set_a = set([i[0] for i in a])
    # 비교해야 하는 인덱스
    comparison_idx = total - set_a
    # a가 선택한것 에서 나올 수 있는 경우의 수
    elem = []
    for e in a:
        elem.append(e[1])

    elem_b = []
    for b in nums:
        if b[0] in comparison_idx:
            elem_b.append(b[1])

    tmp_win = 0
    a_sum, b_sum = Counter(), Counter()
    for x in list(product(*elem)):
        a_sum[sum(x)] += 1

    for x in list(product(*elem_b)):
        b_sum[sum(x)] += 1

    for x in a_sum.keys():
        for y in b_sum.keys():
            if x > y:
                tmp_win += (a_sum[x] * b_sum[y])
    print(tmp_win)


    for x in list(product(*elem)):
        sum1 = sum(x)
        for y in list(product(*elem_b)):
            if sum1 > sum(y):
                win += 1

    if win > ans:
        ans = win
        ans_list = list(set_a)


for i in range(len(ans_list)):
    ans_list[i] += 1
print(ans_list)




