input()
arr = set(map(int, input().split()))
input()
target = list(map(int, input().split()))

for num in target:
    if num in arr:
        print('1')
    else:
        print('0')