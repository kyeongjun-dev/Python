n = int(input())
arr = list()
for _ in range(n):
    arr.append(int(input()))

stack = []
idx = 0

num = 1
answer = []
while idx < n and num <= n+1:
    if len(stack) == 0:
        stack.append(num)
        num += 1
        answer.append('+')
    else:
        if stack[-1] == arr[idx]:
            stack.pop()
            idx += 1
            answer.append('-')
        else:
            stack.append(num)
            num += 1
            answer.append('+')

if len(stack) == 0:
    for c in answer:
        print(c)
else:
    print('NO')