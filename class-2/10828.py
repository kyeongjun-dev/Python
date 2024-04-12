import sys
input = sys.stdin.readline

n = int(input())

stack = list()
for _ in range(n):
    s = input().rstrip()
    if s == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif s == 'size':
        print(len(stack))
    elif s == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif s == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    else:
        word, num = s.split()
        num = int(num)
        stack.append(num)