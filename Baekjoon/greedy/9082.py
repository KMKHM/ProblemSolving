import sys



a = list("23321")

b = list("#####")

check = [0] * len(a)

d = [-1, 0, 1]



while ("3" in a):
    if "3" in a:
        # 인덱스
        idx = a.index("3")
        # 첫번째나 마지막 인덱스가 아니라면
        if idx != 0 or idx != len(a) - 1:
            if not (b[idx-1] == b[idx] == b[idx+1] == "*"):
                # 체크안한 인덱스라면
                if not check[idx]:
                    check[idx] = 1
                    for i in range(3):
                        b[idx + d[i]] = "*"

                else:
                    continue

            if idx == 0:
                b[idx], b[idx+1] = "*", "*"
        a[idx] = 100


print(b)

