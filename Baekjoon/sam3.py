def explore_combinations(a, b, c, i, result):
    if i == len(a):
        # 모든 i에 대한 조합이 완성되면 결과에 추가
        result.append([a[:], b[:], c[:]])
        return

    # 현재 i에 대한 j 값 탐색
    for j in range(len(a[i])):
        # 현재 i의 j 값을 갱신
        a[i][1] = j
        # 다음 i에 대한 재귀 호출
        explore_combinations(a, b, c, i + 1, result)

def generate_all_combinations(a, b, c):
    result = []
    explore_combinations(a, b, c, 0, result)
    return result

# 예시
a = [[3, 4], [2, 3], [1, 2], [0, 1]]
b = [[3, 4], [1, 3], [2, 3], [0, 1]]
c = [[3, 6], [2, 5], [1, 2], [0, 1]]

combinations = generate_all_combinations(a, b, c)

# 결과 출력
for combination in combinations:
    print(combination)
