# https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
arr = list(map(int, input().split()))

l, r, cur = 0, 0, arr[0]
ans = 0

while l <= r < n:
    if cur < m:
        r += 1
        if r < n:
            cur += arr[r]
    elif cur > m:
        cur -= arr[l]
        l += 1
        if r < l < n:
            r = l
            cur = arr[l]
    else:
        ans += 1
        r += 1
        if r < n:
            cur += arr[r]

print(ans)
