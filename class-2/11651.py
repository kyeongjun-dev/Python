import sys
input = sys.stdin.readline

n = int(input())

arr = list()

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))

arr.sort(key=lambda x: (x[1], x[0]))

for a, b in arr:
    print(a, b)