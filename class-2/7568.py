n = int(input())

arr = list()
save = list()
for _ in range(n):
    kg, cm = map(int, input().split())
    arr.append([kg, cm])
    save.append(0)

for i in range(n):
    cnt = 1
    for j in range(n):
        if i==j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    save[i] = str(cnt)

print(" ".join(save))