import sys

input = sys.stdin.readline

d = dict()

for i in range(1, 10001):
    d[i] = 0

n = int(input())

for _ in range(n):
    num = int(input())
    d[num] += 1

for key, value in d.items():
    for _ in range(value):
        print(key)