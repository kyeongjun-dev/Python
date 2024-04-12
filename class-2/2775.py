arr = [
    [ 0 for _ in range(16)] for _ in range(16)
]

for i in range(16):
    arr[0][i] = 1
    arr[i][0] = 1

for j in range(1, 16):
    for i in range(1, 16):
        arr[j][i] = arr[j][i-1] + arr[j-1][i]

for _ in range(int(input())):
    k = int(input()) # 층
    n = int(input()) # 호수
    print(arr[k+1][n-1])