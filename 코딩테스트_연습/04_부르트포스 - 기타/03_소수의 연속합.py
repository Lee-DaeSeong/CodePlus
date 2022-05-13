# https://www.acmicpc.net/problem/1644

import sys
import math

n=int(input())
if n == 1:
    print(0)
    exit()
arr = [True for i in range(n+1)]
primes = []
for i in range(2, int(math.sqrt(n)+1)):
    if arr[i]==True:
        j=2
        while i*j<=n:
            arr[i*j]=False
            j+=1

arr = [i for i in range(n+1) if arr[i] == True and i > 1]

l, r, cur = 0, 0, arr[0]
ans = 0
while l <= r < len(arr):
    if cur < n:
        r += 1
        if r < len(arr):
            cur += arr[r]
    elif cur > n:
        cur -= arr[l]
        l += 1
        if r < l < n:
            r = l
            cur = arr[r]
    else:
        ans += 1
        r += 1
        if r < len(arr):
            cur += arr[r]

print(ans)
