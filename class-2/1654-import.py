k, n = map(int, input().split())
l = list()
for _ in range(k):
    l.append(int(input()))

print(l)
left = 1
right = max(l)

while left <= right:
    mid = (left + right) // 2
    print(left, right, mid)
    result = 0
    for i in range(k):
        result += l[i] // mid

    print('result:', result)
    if result < n:
        right = mid - 1
    elif result >= n:
        left = mid + 1

print(left, right)