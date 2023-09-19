s = "a1b2"
letter = list(s)
res = set()


tmp = []

def bt(idx):
    print(tmp)
    if idx == len(letter)-2:
        print(tmp)

    for i in range(idx, len(res)):
        if letter[i].isdigit():
            if letter[i] not in tmp:
                tmp.append(letter[i])
                bt(idx + 1)
                tmp.pop()
        else:
            if letter[i].lower() not in tmp:
                tmp.append(letter[i].lower())
                bt(idx + 1)
                tmp.pop()
            if letter[i].uppper() not in tmp:
                tmp.append(letter[i].upper())
                bt(idx + 1)
                tmp.pop()

bt(0)
