def solution(string):
    arr = list(string)
    stack = list()
    for c in arr:
        if c == "[" or c =="(":
            stack.append(c)
        elif c == "]" or c ==")":
            if len(stack) == 0:
                print('no')
                return
            if stack and c == "]" and stack[-1] == "(":
                print('no')
                return
            elif stack and c == ")" and stack[-1] == "[":
                print('no')
                return
            else:
                stack.pop()
        else:
            continue
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

while True:
    string = input()
    if string == ".":
        break
    else:
        solution(string)