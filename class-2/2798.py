from itertools import combinations, permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = 0
for c in combinations(arr, 3):
    sum_c = sum(c)
    if sum_c <= m:
        max_sum = max(max_sum, sum_c)
print(max_sum)