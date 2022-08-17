# https://www.acmicpc.net/source/47797872

import collections

n = int(input())
arr = list(map(int, input().split()))

ans = 0

while sum(arr):
    temp = arr[:]

    flag = True
    for i in range(n):
        if arr[i] % 2 == 0:
            temp[i] = arr[i] // 2
        else:
            flag = False
            arr[i] -= 1
            ans += 1

    if flag:
        arr = temp[:]
        ans += 1

print(ans)
