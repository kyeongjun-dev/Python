n = int(input())

flag = True
cnt_5 = 0
cnt_3 = 0
tmp = 0
while n > 0:
    if n % 5 == 0:
        cnt_5 = cnt_5 + (n // 5)
        break
    else:
        cnt_3 += 1
        n -= 3
if n < 0:
    print(-1)
else:
    print(cnt_5 + cnt_3)