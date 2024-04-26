
arr = [[0, 0] for _ in range(41)]

arr[0][0] = 1
arr[0][1] = 0
arr[1][0] = 0
arr[1][1] = 1

for i in range(2, 41):
    arr[i][0] = arr[i-1][0] + arr[i-2][0]
    arr[i][1] = arr[i-1][1] + arr[i-2][1]

t = int(input())
for _ in range(t):
    i = int(input())
    print(arr[i][0], arr[i][1])