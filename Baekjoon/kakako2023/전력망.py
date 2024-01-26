from collections import Counter
def solution(n, wires):
    def find(x):
        if x == parent[x]:
            return x
        return find(parent[x])
    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return
        parent[max(a, b)] = min(a, b)

    ans = 1000000

    for i in range(wires):
        parent = [k for k in range(n + 1)]

        for j in range(len(wires)):
            if j == i:
                continue
            union(wires[j][0], wires[j][1])

        tmp = list(Counter(parent[1:]).values())

        if len(tmp) != 1:
            ans = min(abs(tmp[0] - tmp[1]), ans)
        else:
            return tmp[0]
    return ans
