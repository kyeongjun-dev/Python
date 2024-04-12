from collections import deque
# t = int(input())

def solution():
    n, i = map(int, input().split())
    arr1 = deque(map(int, input().split()))
    arr2 = deque([ x for x in range(len(arr1))])

    cnt = 1
    while True:
        m = max(arr1)
        if arr1[0] == m:
            if arr2[0] == i:
                break
            else:
                arr1.popleft()
                arr2.popleft()
            cnt += 1
        else:
            arr1.append(arr1.popleft())
            arr2.append(arr2.popleft())

    print(cnt)

n = int(input())
for _ in range(n):
    solution()