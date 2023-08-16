s = input().rstrip()


def check(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack[-1] == "(":
                stack.pop()
        elif char == "[":
            stack.append(char)
        elif char == "]":
            if stack[-1] == "[":
                stack.pop()
    return True if len(stack) == 0 else 0

if not check(s):
    print(0)
else:
    res = 0
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        if char == "[":
            stack.append(char)
        if char == ")":
            stack.pop()
            if not stack:
                res *= 2
            else:
                res += 2
        if char == "]":
            stack.pop()
            if not stack:
                res *= 3
            else:
                res += 3
    print(res)
