from collections import Counter

input()
arr = list(map(int, input().split()))
cd = Counter(arr)

s = set(cd.keys())

input()

arr = list(map(int, input().split()))
for n in arr:
    if n in s:
        print(cd[n], end=' ')
    else:
        print('0', end=' ')