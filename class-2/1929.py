m, n = map(int, input().split())
l = [0 for _ in range(1000001)]
l[0] = 1
l[1] = 1
for i in range(2, 1000001):
    tmp = 2
    while i * tmp <= 1000000:
        l[i * tmp] = 1
        tmp += 1

for i in range(m, n+1):
    if l[i] == 0:
        print(i)