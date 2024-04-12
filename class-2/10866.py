import sys
input = sys.stdin.readline

from collections import deque

dq = deque()

n = int(input())

for _ in range(n):
    string = input().rstrip()

    if string == 'pop_front':
        if not dq:
            print(-1)
        else:
            print(dq.popleft())
    elif string == 'pop_back':
        if not dq:
            print(-1)
        else:
            print(dq.pop())
    elif string == 'size':
        print(len(dq))
    elif string == 'empty':
        if not dq:
            print(1)
        else:
            print(0)
    elif string == 'front':
        if not dq:
            print(-1)
        else:
            print(dq[0])
    elif string == 'back':
        if not dq:
            print(-1)
        else:
            print(dq[-1])
    else:
        command, num = string.split()
        num = int(num)
        if command == 'push_back':
            dq.append(num)
        else:
            dq.appendleft(num)
