s1 = "abc de cvd"
s2 = "bcd g fp"
s3 = "abc deo cpl"
s4 = "abc deo cpa"
string1 = ["a b c", "ab bc cd", "ab bc cd", "ab bc cd", "aba bca cda", "abad bcad cdad", "abad bcad cdad",
           "abad bcad cdad", "abad bcad cdad"]

string = ["a b c", "ab bc cd", "ab bc cd", "ab bc cd", "aba bca cda", "abad bcad cdad", "aad bcad cdad",
          "abad bcad cdad", "abad bcad cdad"]

# 전체 문자열 저장 리스트
string1 = [s1, s2, s3, s4]

# 전체 처리해야 할 문자열 길이
n = len(string)

# 정답
res = []


def trans_graph(ls, length):
    graph = [[] for _ in range(length)]
    for char in ls:
        for i in range(len(char)):
            graph[i].append(char[i])
    return graph


for i in range(n):
    s_list = string[i].split()
    temp = 0
    for c in s_list:
        temp = max(temp, len(c))

    s_graph = trans_graph(s_list, temp)
    print(s_graph)

    first = "".join(s_graph[0])

    if first not in res:
        res.append(first)
    else:
        for i in range(1, temp):
            idx = i

            flag = True

            for j in s_graph[i]:
                first = first[:idx] + j + first[idx:]
                if first not in res:
                    res.append(first)
                    flag = False
                    break
                idx += (i + 1)
            if not flag:
                break

print(res)