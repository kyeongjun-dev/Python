input()
arr = list(map(int, input().split()))

max_num = max(arr)
check = [ 0 for _ in range(max_num+1)]

for n in range(2, max_num+1):
    tmp = 2
    while n*tmp <= max_num:
        check[n*tmp] = 1
        tmp += 1

check[1] = 1 
cnt = 0
for num in arr:
    if check[num] == 0:
        cnt += 1
print(cnt)

# cnt = 0
# for num in arr:
