n = int(input())

arr = list()

for _ in range(n):
    age, name = input().split()
    age = int(age)
    arr.append((age, name))

arr.sort(key=lambda x: x[0])
for age, name in arr:
    print(age, name)