import sys
from collections import deque
input = sys.stdin.readline

dq = deque()

n = int(input())

for _ in range(n):
    s = input().strip()
    if s == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif s == 'size':
        print(len(dq))
    elif s == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif s == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif s == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    else:
        word, num = s.split()
        num = int(num)
        dq.append(num)