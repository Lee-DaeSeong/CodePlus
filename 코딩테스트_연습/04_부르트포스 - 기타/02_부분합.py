# https://www.acmicpc.net/problem/1806

import sys
import math

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

l, r, cur = 0, 0, arr[0]
ans = math.inf

while l <= r < n:
    if cur < m:
        r += 1
        if r < n:
            cur += arr[r]
    elif cur > m:
        ans = min(ans, r - l + 1)
        cur -= arr[l]
        l += 1
        if r < l < n:
            r = l
            cur = arr[r]
    else:
        ans = min(ans, r - l + 1)
        r += 1
        if r < n:
            cur += arr[r]

if ans == math.inf:
    ans = 0
print(ans)
