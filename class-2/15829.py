input()
s = list(input())

total = 0

cnt = 0
for c in s:
    num = ord(c) - 96
    total = total + ((num) * (31**cnt))
    cnt+=1

print(total%1234567891)