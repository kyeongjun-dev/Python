input()
l = list(map(int, input().split()))
m = max(l)
result = 0
for i in range(len(l)):
    l[i] = (l[i] / m) * 100
print(sum(l)/len(l))