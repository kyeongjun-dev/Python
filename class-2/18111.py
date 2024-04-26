import sys
input = sys.stdin.readline
n, m, block = map(int, input().split())

arr = list()
max_layer = 0
min_layer = 1e9
for _ in range(n):
    layer = list(map(int, input().split()))
    arr += layer

from collections import Counter

cd = Counter(arr)

max_layer = max(arr)
min_layer = min(arr)

result_t = 1e9
result_h = 0

for height in range(min_layer, max_layer+1):
    b = 0
    t = 0

    for key, value in cd.items():
        if key > height:
            b += (key - height)*value
            t += 2 * (key - height) * value
        elif key < height:
            b -= (height - key)*value
            t += (height - key)*value

    if b + block >= 0:
        if t <= result_t:
            result_t = t
            result_h = height
print(result_t, result_h)