from collections import deque

n, k = map(int, input().split())

dq = deque([i for i in range(1, n+1)])

cnt = 1
result = list()
while dq:
    if cnt % (k+1) == 0:
        result.append(str(dq.pop()))
    else:
        poped = dq.popleft()
        dq.append(poped)
    cnt += 1

print("<", end='')
print(", ".join(result), end='')
print(">")