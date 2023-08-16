"""
Union-Find
"""

# 노드의 수와 union연산의 수 입력
v, e = map(int, input().split())

parent = [0] * (v+1)

# 특정 원소가 속한 집합 찾기 => 루트 노드 반환
def find_parent(parent, x):
    # 만약 루트노드가 아니라면, 루트노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def find_parent2(parent, x):
    if parent[x] != x:
        parent[x] = find_parent2(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모 테이블을 부모 노드를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union연산을 e 번 시행
for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end="")
for i in range(1, v+1):
    print(find_parent(parent, i), end="")

print()

print("부모 테이블: ", end="")
for i in range(1, v+1):
    print(parent[i], end="")
