n = int(input())

for _ in range(n):
    check = True
    arr = list(input())
    stack = list()
    for c in arr:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                check = False
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                check = False
                break
    
    if check == False or len(stack) != 0:
        print('NO')
    else:
        print('YES')