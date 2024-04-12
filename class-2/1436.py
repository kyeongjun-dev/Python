n = int(input())
cnt = 0
start = '666'
while cnt != n:
    if '666' in start:
        cnt += 1
        start = int(start) + 1
        start = str(start)
    else:
        start = int(start) + 1
        start = str(start)
print(int(start)-1)

###
n = int(input())
cnt = 0
num = 1
while cnt != n:
    if '666' in str(num):
        cnt += 1
    num += 1
print(num-1)