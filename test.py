from itertools import product, permutations
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
rate = [10, 20, 30, 40]

emoticons = [1300, 1500, 1600, 4900]

def solution(users, emoticons):
    # 할인율
    rate = [10, 20, 30, 40]

    # 이모티콘 갯수
    n = len(emoticons)

    # 할인율 조합
    possible = list(product(rate, repeat=n))

    # 최대 가입자 수, 최대 수입
    max_val, max_cost = -1, -1

    # 각 할인율 조합 탐색
    for element in possible:
        # 가입자수, 수익 초기화
        service, revenue = 0, 0
        # 유저의 제한 비율, 제한 비용 탐색
        for limit_rate, limit_cost in users:
            # 각 유저가 구매하는 미용
            temp_cost = 0
            for j in range(len(element)):
                if limit_rate <= element[j]:
                    temp_cost += emoticons[j] * (100 - element[j]) // 100
                # 제한 비용넘어서면 더 이상 탐색X
                if temp_cost >= limit_cost:
                    break

            if temp_cost >= limit_cost:
                service += 1
            else:
                revenue += temp_cost

        # 무지성으로 수익 최대화하면 정답이 최대 이용자수와 관계없이 최대 수익으로 나온다.
        if max_val <= service:
            if service == max_val:
                # 같은 이용자 수일 경우에는 수익 갱신
                max_cost = max(max_cost, revenue)
            else:
                # 더 많을 때는 수익 그대로 넣어주면 된다.
                max_cost = revenue
            max_val = service


    return [max_val, max_cost]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))