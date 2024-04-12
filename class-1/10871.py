a, b = map(int, input().split())
l = list(map(int, input().split()))
save = list()
for n in l:
    if n < b:
        save.append(str(n))
print(' '.join(save))