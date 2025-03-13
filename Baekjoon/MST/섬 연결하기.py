def solution(n, costs):
    if n == 1:
        return 0
    # 정답
    answer = 0

    # 부모 테이블
    parent = [i for i in range(n)]

    # find
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    # union
    def union(a, b):
        root_a, root_b = find(a), find(b)

        if root_a == root_b:
            return

        parent[max(root_a, root_b)] = min(root_a, root_b)

    costs.sort(key=lambda x: x[2])

    # 크루스칼
    for a, b, c in costs:
        if find(a) != find(b):
            union(a, b)
            answer += c

    return answer