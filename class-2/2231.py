n = int(input())
check = False
for num in range(1, n+1):
    s = str(num)
    l = len(s)
    div = 1
    result = 0
    for _ in range(l):
        result += (num//div) % (10)
        div *= 10
    if result + num == n:
        print(num)
        check = True
        break

if check == False:
    print(0)