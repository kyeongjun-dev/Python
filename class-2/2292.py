n = int(input())
s = 1
cnt = 6
point = 1
while True:
    if n <= s:
        print(point)
        break
    s = s + cnt
    cnt = cnt + 6
    point += 1