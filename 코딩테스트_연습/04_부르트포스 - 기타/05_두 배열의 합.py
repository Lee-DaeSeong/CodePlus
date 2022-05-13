# https://www.acmicpc.net/problem/2143
import collections

target = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

x = []
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += a[j]
        x.append(temp)

y = []
for i in range(m):
    temp = 0
    for j in range(i, m):
        temp += b[j]
        y.append(temp)

x.sort()
y.sort()

cnt = collections.Counter(y)

ans = 0
for i in x:
    ans += cnt[target-i]

print(ans)