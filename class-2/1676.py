n = int(input())
fac = 1
for i in range(1, n+1):
    fac = fac * i
fac = list(str(fac))
cnt = 0
for i in range(len(fac)-1, 0, -1):
    if fac[i] =='0':
        cnt += 1
    else:
        break
print(cnt)
