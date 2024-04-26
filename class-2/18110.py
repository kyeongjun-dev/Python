import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    exit()
arr = list()

for _ in range(n):
    score = int(input())
    arr.append(score)

arr.sort()
from collections import deque

dq = deque(arr)

import math

cut = math.floor((n * 0.15) + 0.5)
for _ in range(cut):
    dq.popleft()
    dq.pop()

result = math.floor(sum(dq)/len(dq) + 0.5)
print(result)