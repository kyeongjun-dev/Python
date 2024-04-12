import sys
n = int(input())
result_sum = 0
d = dict()
s = set()
arr = list()
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
    result_sum += num
    if num in s:
        d[num] += 1
    else:
        d[num] = 1
        s.add(num)


arr.sort()

# 산술평균
print(round(result_sum/n))

# 중앙값
print(arr[n//2])

l = list()
max_num = max(d.values())
for key, value in d.items():
    if value == max_num:
        l.append(key)

# 최빈값
if len(l) >= 2:
    l.sort()
    print(l[1])
else:
    print(l[0])

# 범위
print(abs(arr[-1] - arr[0]))