s = input().rstrip()
t = input().rstrip()

flag = False

def backtraccking(string):

    global flag

    if flag:
        return

    if string not in t and string[::-1] not in t:
        return

    if len(string) == len(t):
        if string == t:
            flag = True
        return

    backtraccking(string+"A")
    backtraccking((string+"B")[::-1])

backtraccking(s)

print(1 if flag else 0)