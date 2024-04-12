input()
arr = list(map(int, input().split()))
arr.sort()
input()
target = list(map(int, input().split()))

for num in target:
    start = 0
    end = len(arr) -1
    flag = False
    while start <= end:
        mid = (start + end) // 2
        if num < arr[mid]:
            end = mid - 1
        elif num > arr[mid]:
            start = mid + 1
        else:
            flag = True
            break
    if flag:
        print("1")
    else:
        print("0")