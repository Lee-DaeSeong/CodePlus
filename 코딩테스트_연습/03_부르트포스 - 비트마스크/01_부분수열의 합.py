# https://www.acmicpc.net/problem/14225

n = int(input())
arr = list(map(int, input().split()))

check = [False] * (100000 * 20)

for i in range(1 << n):
    cur = 0
    for j in range(n):
        if (i&(1<<j)):
            cur += arr[j]
    check[cur] = True

print(check.index(False))
