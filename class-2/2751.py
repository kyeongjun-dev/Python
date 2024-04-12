import sys

n = int(input())
arr = list()
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for n in arr:
    print(n)