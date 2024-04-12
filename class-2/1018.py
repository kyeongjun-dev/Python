arr_b = [
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB')
]

arr_w = [
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW'),
    list('WBWBWBWB'),
    list('BWBWBWBW')
]

y, x = map(int, input().split())
arr = list()

for _ in range(y):
    arr.append(list(input()))

res = 2500
for j in range(0, y-7):
    for i in range(0, x-7):
        start = [j, i]
        b_cnt = 0
        w_cnt = 0
        for l in range(8):
            for k in range(8):
                if arr[j+l][i+k] != arr_b[l][k]:
                    b_cnt += 1
                if arr[j+l][i+k] != arr_w[l][k]:
                    w_cnt += 1
        res = min(res, min(b_cnt, w_cnt))
print(res)
