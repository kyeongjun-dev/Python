n = int(input())
l = list()
s = set()
for _ in range(n):
    string = input()
    if string not in s:
        s.add(string)
        l.append(string)

l.sort(key= lambda x: (len(x), x))

for string in l:
    print(string)