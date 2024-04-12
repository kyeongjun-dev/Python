while True:
    s = input()
    if s == '0':
        break
    l = list(s)
    left = 0
    right = len(l) -1
    while left <= right:
        if l[left] == l[right]:
            left += 1
            right -= 1
            continue
        else:
            break
    if left > right:
        print('yes')
    else:
        print('no')